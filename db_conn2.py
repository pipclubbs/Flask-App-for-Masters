""" class to input data into the SQLite3 database
    data comes in from the scrapers and on initialisation 
    is sorted into a list depending on type of data before
    being sent to a method to insert data into the database """

import sqlite3
import os


class DatabaseConnection:
    """ initialise a class instance:
        check if the scraped data was from a centre or class
        search, add it to a list, and send it to the 
        correct class method for insertion into the
        database """

    def __init__(self, input_value):
        if isinstance(input_value, str):
            self.data_string = input_value
            check_centres = self.check_centre_table(self.data_string)
            check_classes = self.check_class_table(self.data_string)
            print("this shouldn't fire so if it does something has gone horribly wrong!")

        elif isinstance(input_value, list):
            self.data_list = input_value
            self.create_tables()
            data = []
            data2 = []
            for data_dict in self.data_list:
                # check if the data_list has come from a centre or class search
                if 'title' not in data_dict:
                    # if 'title' isn't there it is centre data
                    data.append(data_dict)
                else:
                    # if it is it is class data
                    data2.append(data_dict)

            if len(data) > 0:
                # check if values were added to data
                self.insert_centre_data(data)
            else:
                self.insert_data(data2)

        else:
            raise ValueError("Input must be a string or a list")

    """create a database file and the tables"""

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
        print("database and tables created successfully")
        conn.close()

    def check_centre_table(self, area):
        searched_area = area
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM centres WHERE area = ? ", (searched_area))
        find = cur.fetchall()

        return any(row[0] == searched_area for row in find)

    def check_class_table(self, area):
        searched_area = area
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM classes WHERE area = ? ", (searched_area))
        find = cur.fetchall()

        return any(row[0] == searched_area for row in find)

    """method to check whether the row already exists for 
        a centre. Return is a Boolean that tells the 
        insert_centre_data() method which insert statement to 
        execute """

    def check_rows_exist(self, data):
        input_data = data
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        for row in input_data:
            area_from_data = row["area"]
            name_from_data = row["name"]

        cur.execute(
            "SELECT * FROM centres WHERE area = ? AND name = ?", (area_from_data, name_from_data))
        find = cur.fetchall()

        # use a generator expression with any() to check if there are any rows that contain the name and row
        return any(row[0] == area_from_data and row[1] == name_from_data for row in find)

    """ method to insert class data into the classes and centre tables"""
    # need to update this so that it doesn't overwrite the values if the
    # centre already exists

    def insert_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        check = self.check_rows_exist(data)

        if check == False:
            cur.executemany('''INSERT OR REPLACE INTO centres (
                        area, name, classUrl
                        ) VALUES (
                        :area, :name, :classUrl);
                        ''', data)

        else:
            cur.executemany(
                '''UPDATE centres SET classUrl = :classUrl WHERE name =:name;''', data)

        cur.executemany('''INSERT or REPLACE INTO classes (
                            area, classUrl, title, description
                            ) VALUES (
                            :area, :classUrl, :title, :description);
                            ''', data
                        )
        conn.commit()
        # print("Records successfully added")
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

    def remove_db():
        """function to remove database after process has completed so that it can begin again"""
        user_input = input(f"\ndo you want to remove the database?")
        if user_input == "y":
            os.remove("database.db")
        else:
            return
