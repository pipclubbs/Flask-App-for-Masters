import sqlite3
import os

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


test_dict = [
    {
        "name": "The Pool",
        "url": "www.thepool.com",
        "title": "this class",
        "description": "description 1"
    },
    {
        "name": "The Pool",
        "url": "www.thepool.com",
        "title": "that class",
        "description": "description 2"
    },
    {
        "name": "The Pool",
        "url": "www.thepool.com",
        "title": "that class",
        "description": "description 3"
    },
    {
        "name": "The Pool1",
        "url": "www.thepool1.com",
        "title": "also this class",
        "description": "description 4"
    }
]

cur = conn.cursor()
cur.executemany(
    'INSERT OR REPLACE INTO centres (name, url) VALUES (:name, :url);', test_dict)
cur.executemany(
    'INSERT or replace INTO classes (url, title, description) VALUES (:url, :title, :description);', test_dict)

conn.commit()
print("Records successfully added")

cursor = conn.execute(
    "SELECT * FROM classes LEFT JOIN centres USING (url);")

for row in cursor:
    print(row)

name = ''
url = ''
title = ''
description = []

for row in cursor:
    if row[3] != name:
        name = row[3]
        print(f'\n{name}')

    if row[0] != url:
        url = row[0]
        print(url)

    if row[1] != title:
        title = row[1]
        print(f'\n{title}')

    description.append(row[2])
    for d in description:
        print(d)
        description = []
        continue

conn.close()


def remove_db():
    """function to remove database after process has completed so that it can begin again"""
    user_input = input(f"\ndo you want to remove the database?")
    if user_input == "y":
        os.remove("database.db")
    else:
        return


remove_db()
