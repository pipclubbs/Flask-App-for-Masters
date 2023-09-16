from bs4 import BeautifulSoup
import requests
# import json
# import database_connection

import sqlite3
import os

"""This script requests the html for the classes page at Climb Newcastle,
and returns the relevant sorted scraped data to a json file"""
# class NorthEastClasses() {
url = "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h1():
    """search the html for an <h1> tag and return the content"""
    h1_tag = soup.find('h1')
    h1_tag = h1_tag.string
    return h1_tag


def find_h4():
    """search the html for <h4> tags and return the content as a list"""
    h4_tag = soup.find_all('h4')
    h4_tag_list = [e.string for e in h4_tag]
    return h4_tag_list


def final_p_list(p_tags):
    p_tags = p_tags
    list_1 = []
    for p in p_tags:
        if p != None and "shopping cart" not in p and "Climb Newcastle Ltd" not in p and "Pick a date" not in p:
            list_1.append(p)
    return list_1


def find_p():
    """search the html for <p> tags and return the content as a list
    to another function that will remove unnecessary list items"""
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    return final_p_list(p_tag_list)


"""run the functions above and assign the returned values to a dictionary"""
find_h1 = find_h1()
find_h4 = find_h4()
find_p = find_p()
# print(find_p)

valley_classes = [
    {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h1,
        "description": find_p[0]
    }, {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h4[0],
        "description": find_p[1],
    }, {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h4[1],
        "description": find_p[2]
    }, {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h4[2],
        "description": find_p[3]
    }, {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h4[2],
        "description": find_p[4]
    }, {
        "name": "Climb Valley, Newcastle",
        "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
        "title": find_h4[2],
        "description": find_p[5]
    }

]

"""convert dictionary to json and append to external json file
with open("saved_classes.json", "a") as file:
    json.dump(valley_classes, file, indent=4)"""
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

cur = conn.cursor()
cur.executemany(
    'INSERT OR REPLACE INTO centres (name, url) VALUES (:name, :url);', valley_classes)
cur.executemany(
    'INSERT or replace INTO classes (url, title, description) VALUES (:url, :title, :description);', valley_classes)

conn.commit()
print("Records successfully added")

cursor = conn.execute(
    "SELECT * FROM classes LEFT JOIN centres USING (url);")

# for row in cursor:
#    print(row)

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
