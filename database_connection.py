import sqlite3

conn = sqlite3.connect(':memory:')
print("database opened successfully")

conn.execute('CREATE TABLE centres (name TEXT, url TEXT)')
print("database table created successfully")
conn.execute('CREATE TABLE classes (url TEXT, title TEXT, description TEXT)')
print("database table created successfully")

cur = conn.cursor()
cur.execute(
    'INSERT INTO centres (name, url) VALUES ("The Pool", "www.thepool.com")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "this class", "description 1")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "this class", "description 2")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "this class", "description 3")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "this class", "description 4")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "this class", "description 5")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "that class", "description 6")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "that class", "description 7")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "that class", "description 8")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "that class", "description 9")')
cur.execute(
    'INSERT INTO classes (url, title, description) VALUES ("www.thepool.com", "that class", "description 0")')

conn.commit()
print("Records successfully added")

cursor = conn.execute(
    "select title, description from classes where url = 'www.thepool.com'")
title = ""
description = []
for row in cursor:
    if row[0] != title:
        title = row[0]
        print(title)

    description.append(row[1])
    for d in description:
        print(d)
    description = []
    continue
