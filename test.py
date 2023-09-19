import sqlite3

conn = sqlite3.connect('database.db')
data = conn.execute(
    "SELECT name, classUrl, title, description FROM classes LEFT JOIN centres USING (classUrl);")
# for i in data:
#    print(i)

name = ''
url = ''
title = ''
description = []
list_of_classes = []
# for row in data:
# print(row)
for row in data:
    if row[0] != name:
        name = (f'{row[0]}')
        # list_of_classes.append(f'\n\n{name}')
        print(f'\n{name}')
    if row[1] != url:
        url = row[1]
        # list_of_classes.append(url)
        print(url)
    if row[2] != title:
        title = (row[2])
        # list_of_classes.append(f'\n{title}')
        print(f'\n{title}')
    description.append(row[3])
    for d in description:
        # list_of_classes.append(d)
        print(d)
        description = []
        continue

conn.close()
