""" class to input data into the SQLite3 database
    data comes in from the scrapers and on initialisation 
    is sorted into a list depending on type of data before
    being sent to a method to insert data into the database """

import sqlite3
import os
import datetime


class DatabaseConnection:
    """ initialise a class instance:
        check if the scraped data was from a centre or class
        search, add it to a list, and send it to the 
        correct class method for insertion into the
        database """

    def __init__(self, input_value):
        self.data_list = input_value

        self.create_tables()

        # print(f'data_list: {self.data_list}')
        centre_data = []  # empty list to append centre only data to
        class_and_centre_data = []  # empty list to append class and centre data to
        club_data = []  # empty list to append club data to
        event_data = []  # empty list to append event data to

        for data_dict in self.data_list:
            # print(f'data_dict: {data_dict}')
            # check if the data_list has come from a centre or class search
            if 'title' not in data_dict:
                # if 'title' isn't there it is centre data
                # put the data into the centre only list
                centre_data.append(data_dict)

            elif 'type' not in data_dict and 'event' not in data_dict:
                # if it is there it is class data
                # put the data into the class and centre list
                class_and_centre_data.append(data_dict)

            elif 'event' not in data_dict:
                club_data.append(data_dict)

            else:
                event_data.append(data_dict)

        if centre_data:
            self.insert_centre_data(centre_data)
        elif class_and_centre_data:
            self.insert_data(class_and_centre_data)
        elif club_data:
            # print(f'the data is {club_data}')
            self.insert_club_data(club_data)
        elif event_data:
            self.insert_event_data(event_data)
        else:
            return

    """create a database file and the tables"""

    def return_check(self, check_result):
        if check_result:
            print("this is true here")
            return True
        else:
            print("this is false")
            return False

    def create_tables(self):
        # os.remove("database.db")
        conn = sqlite3.connect('database.db')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS centres (
                     area TEXT NOT NULL, name TEXT UNIQUE NOT NULL,
                     homeUrl TEXT, contactUrl TEXt, classUrl TEXT, 
                     street TEXT, street_area TEXT, city TEXT, 
                     postcode TEXT, email TEXT, phone NUM,
                     created TIMESTAMP NOT NULL)
                     ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS classes (
                     area TEXT NOT NULL, classUrl TEXT NOT NULL, 
                     title TEXT, description TEXT UNIQUE,
                     created TIMESTAMP NOT NULL)
                     ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS clubs (
                     area TEXT NOT NULL, name TEXT NOT NULL, url TEXT NOT NULL,
                     intro TEXT, title TEXT, subtitle TEXT, description TEXT UNIQUE,
                     created TIMESTAMP NOT NULL)
                     ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS events (
                    name TEXT NOT NULL, url NOT NULL, intro TEXT, title TEXT, 
                    subtitle TEXT, description TEXT UNIQUE,
                    created TIMESTAMP NOT NULL)
                     ''')
        print("database and tables created successfully")
        conn.close()

    """method to check whether the row already exists for 
        a centre. Return is a Boolean that tells the 
        insert_centre_data() method which insert statement to 
        execute """

    def check_rows_exist(self, data):
        input_data = data
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        found_rows = []
        for row in input_data:
            # print(f'check rows exist row: {row}')
            area_from_data = row["area"]
            name_from_data = row["name"]
            # print(f'assigned values {area_from_data}, {name_from_data}')

            cur.execute(
                "SELECT * FROM centres WHERE area = ? AND name = ?", (area_from_data, name_from_data))
            find = cur.fetchall()

            for row in find:
                if row[0] == area_from_data and row[1] == name_from_data:
                    found_rows.append(row)

        if found_rows:
            return True
        else:
            return False

    """ method to insert class data into the classes and centre tables"""
    # need to update this so that it doesn't overwrite the values if the
    # centre already exists

    def insert_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        check = self.check_rows_exist(data)
        if not check:
            cur.executemany('''INSERT OR REPLACE INTO centres (
                        area, name, classUrl, created
                        ) VALUES (
                        :area, :name, :classUrl, :created);
                        ''', data)

            print('new centre added')
        else:
            cur.executemany(
                '''UPDATE centres SET classUrl = :classUrl, created = :created WHERE name =:name;''', data)
            print('centre updated')

        cur.executemany('''INSERT or REPLACE INTO classes (
                            area, classUrl, title, description, created
                            ) VALUES (
                            :area, :classUrl, :title, :description, :created);
                            ''', data
                        )
        print('classes added')
        conn.commit()
        print("Records successfully added")
        conn.close()

    def insert_centre_data(self, data_to_insert):
        data = data_to_insert
        # classUrl may exist in the database - don't want to overwrite it
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        # will be true if the area and name are in a line on the database
        check = self.check_rows_exist(data)
        if check == True:
            # If classUrl in the incoming data is '' it is from centre search. if the class search is already done, the name will be there
            cur.executemany('''
                    UPDATE centres SET homeUrl = :homeUrl, contactUrl = :contactUrl, street = :street, 
                    street_area = :street_area, city = :city, postcode = :postcode, email = :email, phone = :phone, created = :created 
                            WHERE name = :name;''', data)

        else:
            # centre doesn't exist in table insert all values as a new line
            cur.executemany('''INSERT INTO centres (area, name, homeUrl, contactUrl, street,
                            street_area, city, postcode, email, phone, created) VALUES (:area, :name, :homeUrl, :contactUrl, :street,
                            :street_area, :city, :postcode, :email, :phone, :created);''', data)

        conn.commit()
        print("Records successfully added")
        conn.close()

    def insert_club_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany('''INSERT OR REPLACE INTO clubs (area, name, url, intro, title, subtitle, description, created) 
                        VALUES (:area, :name, :url, :intro, :title, :subtitle, :description, :created);''', data)

        conn.commit()
        print("Records successfully added")
        conn.close()

    def insert_event_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany('''INSERT OR REPLACE INTO events (name, url, intro, title, subtitle, description, created) 
                        VALUES (:name, :url, :intro, :title, :subtitle, :description, :created);''', data)

        conn.commit()
        print("Records successfully added")
        conn.close()

    def remove_db():
        """function to remove database after process has completed so that it can begin again"""
        user_input = input(f"\ndo you want to remove the database?")
        if user_input == "y":
            os.remove("database.db")
        else:
            return
