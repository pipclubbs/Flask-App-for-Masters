""" class to input data into the SQLite3 database
    data comes in from the scrapers and on initialisation 
    is sorted into a list depending on type of data before
    being sent to a method to insert data into the database """

import sqlite3
import os
print("SQLite Version:", sqlite3.sqlite_version)


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
        data = []  # empty list to append centre only data to
        data2 = []  # empty list to append class and centre data to
        data3 = []  # empty list to append club data to
        for data_dict in self.data_list:
            print(f'data_dict: {data_dict}')
            # check if the data_list has come from a centre or class search
            if 'title' not in data_dict:
                # if 'title' isn't there it is centre data
                # put the data into the centre only list
                data.append(data_dict)

            elif 'type' not in data_dict:
                # if it is there it is class data
                # put the data into the class and centre list
                data2.append(data_dict)

            else:
                data3.append(data_dict)

        if data:
            self.insert_centre_data(data)
        elif data2:
            self.insert_data(data2)
        elif data3:
            print(f'the data is {data3}')
            self.insert_club_data(data3)

        '''else:
            raise ValueError("Input must be a string or a list")'''

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
                     postcode TEXT, email TEXT, phone NUM)
                     ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS classes (
                     area TEXT NOT NULL, classUrl TEXT NOT NULL, 
                     title TEXT, description TEXT UNIQUE)
                     ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS clubs (
                     area TEXT NOT NULL, name TEXT NOT NULL, url TEXT NOT NULL,
                     intro TEXT, title TEXT, subtitle TEXT, description TEXT UNIQUE)
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
        print('check_rows_exist_is_running')
        print(f'input data: {input_data}')

        found_rows = []
        for row in input_data:
            print(f'check rows exist row: {row}')
            area_from_data = row["area"]
            name_from_data = row["name"]
            print(f'assigned values {area_from_data}, {name_from_data}')

            cur.execute(
                "SELECT * FROM centres WHERE area = ? AND name = ?", (area_from_data, name_from_data))
            find = cur.fetchall()
            # for row in find:
            # print(f'find:{row[0]} and {row[1]}')
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

        print(f'data in insert data is: {data}')
        for row in data:
            print(f'row in insert_data: {row}')
            check = self.check_rows_exist(data)
            print(f'check value is {check}')
            if not check:
                cur.executemany('''INSERT OR REPLACE INTO centres (
                            area, name, classUrl
                            ) VALUES (
                            :area, :name, :classUrl);
                            ''', data)
                print('new centre added')
            else:
                cur.executemany(
                    '''UPDATE centres SET classUrl = :classUrl WHERE name =:name;''', data)
                print('centre updated')

            cur.executemany('''INSERT or REPLACE INTO classes (
                                area, classUrl, title, description
                                ) VALUES (
                                :area, :classUrl, :title, :description);
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
        print(f'the check to see if the rows already existed came out {check}')

        if check == True:
            # If classUrl in the incoming data is '' it is from centre search. if the class search is already done, the name will be there
            cur.executemany('''
                    UPDATE centres SET homeUrl = :homeUrl, contactUrl = :contactUrl, street = :street, 
                    street_area = :street_area, city = :city, postcode = :postcode, email = :email, phone = :phone 
                            WHERE name = :name;''', data)

        else:
            # centre doesn't exist in table insert all values as a new line
            cur.executemany('''INSERT INTO centres (area, name, homeUrl, contactUrl, street,
                            street_area, city, postcode, email, phone) VALUES (:area, :name, :homeUrl, :contactUrl, :street,
                            :street_area, :city, :postcode, :email, :phone);''', data)

        conn.commit()
        print("Records successfully added")
        conn.close()

    def insert_club_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany('''INSERT OR REPLACE INTO clubs (area, name, url, intro, title, subtitle, description) 
                        VALUES (:area, :name, :url, :intro, :title, :subtitle, :description);''', data)

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
