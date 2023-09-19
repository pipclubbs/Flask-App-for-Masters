import sqlite3
import os


class DatabaseConnection:

    def __init__(self, scraped_data):
        self.data_list = scraped_data
        print(self.data_list)
        self.create_tables()
        if "classUrl" not in self.data_list:
            self.insert_centre_data(self.data_list)
        else:
            self.insert_data(self.data_list)

    def create_tables(self):
        # os.remove("database.db")
        conn = sqlite3.connect('database.db')
        print("database created successfully")

        try:
            conn.execute(
                'CREATE TABLE centres (area TEXT NOT NULL, name TEXT UNIQUE NOT NULL, homeUrl TEXT, contactUrl TEXt, classUrl TEXT, street TEXT, street_area TEXT, city TEXT, postcode TEXT, email TEXT, phone NUM)')
            conn.execute(
                'CREATE TABLE classes (classUrl TEXT NOT NULL, title TEXT, description TEXT UNIQUE)')
            print("database tables created successfully")
        except:
            print("database already exists")
        conn.close()

    def insert_data(self, data_to_insert):
        data_list = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany(
            'INSERT OR REPLACE INTO centres (area, name, homeUrl, contactUrl, classUrl, street, street_area, city, postcode, email, phone) VALUES (:area, :name, :homeUrl, :contactUrl, :classUrl, :street, :street_area, :city, :postcode, :email, :phone);', data_list)
        cur.executemany(
            'INSERT or REPLACE INTO classes (area, classUrl, title, description) VALUES (:area, :classUrl, :title, :description);', data_list)
        conn.commit()
        print("Records successfully added")
        conn.close()

    def insert_centre_data(self, data_to_insert):
        data_list = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany(
            'INSERT OR REPLACE INTO centres (area, name, homeUrl, contactUrl, classUrl, street, street_area, city, postcode, email, phone) VALUES (:area, :name, :homeUrl, :contactUrl, :classUrl, :street, :street_area, :city, :postcode, :email, :phone);', data_list)
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
