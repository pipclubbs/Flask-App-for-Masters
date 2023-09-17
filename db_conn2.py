import sqlite3
import os


class DatabaseConnection:

    def __init__(self, scraped_data):
        self.class_list = scraped_data
        self.create_tables()
        self.insert_data(self.class_list)

    def create_tables(self):
        conn = sqlite3.connect('database.db')
        print("database opened successfully")

        try:
            conn.execute(
                'CREATE TABLE centres (name TEXT UNIQUE, url TEXT)')
            conn.execute(
                'CREATE TABLE classes (url TEXT, title TEXT, description TEXT unique)')
            print("database tables created successfully")
        except:
            print("database already exists")

        conn.close()

    def insert_data(self, data_to_insert):
        class_list = data_to_insert
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.executemany(
            'INSERT OR REPLACE INTO centres (name, url) VALUES (:name, :url);', class_list)
        cur.executemany(
            'INSERT or REPLACE INTO classes (url, title, description) VALUES (:url, :title, :description);', class_list)
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
