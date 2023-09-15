import sqlite3
import os

# import northeast_classes

# class_list = northeast_classes.NorthEastClasses()
# class_list = class_list.assign_values()
# for i in class_list:
#    print(i)


class DatabaseConnection:

    def __init__(self, scraped_data):
        self.class_list = scraped_data
        self.create_tables()
        self.insert_data(self.class_list)
        # self.conn = conn

        # self.print_out = self.extract_data()

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
            'INSERT or replace INTO classes (url, title, description) VALUES (:url, :title, :description);', class_list)
        conn.commit()
        print("Records successfully added")
        conn.close()

    """ def extract_data(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.execute(
            "SELECT * FROM classes LEFT JOIN centres USING (url);")
        return self.class_printout(cursor)
        # for row in cursor:
        #    print(row)
def class_printout(self, extracted_data):
        data = extracted_data
        conn = sqlite3.connect('database.db')
        name = ''
        url = ''
        title = ''
        description = []
        list_of_classes = []

        for row in data:
            if row[3] != name:
                name = row[3]
                # print(f'\n{name}')

            if row[0] != url:
                url = row[0]
                # print(url)

            if row[1] != title:
                title = row[1]
                # print(f'\n{title}')

            description.append(row[2])
            for d in description:
                description = d
                continue

            list_of_classes.append(f"\n{name}\n{url}\n{title}\n{description}")
            description = []
        print(f'db_conn: {type(list_of_classes)}')
        print(list_of_classes)
        conn.close()
        return list_of_classes
"""
    def remove_db():
        """function to remove database after process has completed so that it can begin again"""
        user_input = input(f"\ndo you want to remove the database?")
        if user_input == "y":
            os.remove("database.db")
        else:
            return


# remove_db()
