import sqlite3
import os


class DatabaseConnection:

    def __init__(self, scraped_data):
        self.data_list = scraped_data
        self.create_tables()
        data = []
        data2 = []
        for data_dict in self.data_list:
            if 'title' not in data_dict:
                data.append(data_dict)
            else:
                data2.append(data_dict)

        if len(data) > 0:
            self.insert_centre_data(data)
        else:
            self.insert_data(data2)

    def create_tables(self):
        # os.remove("database.db")
        conn = sqlite3.connect('database.db')
        print("database created successfully")

        conn.execute(
            'CREATE TABLE IF NOT EXISTS centres (area TEXT NOT NULL, name TEXT UNIQUE NOT NULL, homeUrl TEXT, contactUrl TEXt, classUrl TEXT, street TEXT, street_area TEXT, city TEXT, postcode TEXT, email TEXT, phone NUM)')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS classes (area TEXT NOT NULL, classUrl TEXT NOT NULL, title TEXT, description TEXT UNIQUE)')
        print("database tables created successfully")
        conn.close()

    def insert_data(self, data_to_insert):
        data = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany('''INSERT OR REPLACE INTO centres (
                        area, name, classUrl
                        ) VALUES (
                        :area, :name, :classUrl);
                        ''', data
                        )
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
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.executemany('''
                        INSERT OR REPLACE INTO centres (
                        area, name, homeUrl, contactUrl, street, 
                        street_area, city, postcode, email, phone
                        ) VALUES (:area, :name, :homeUrl, :contactUrl, 
                        :street, :street_area, :city, :postcode, :email, :phone
                        );
                        ''', data
                        )
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
