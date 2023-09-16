from bs4 import BeautifulSoup
import requests
import sqlite3

url = "https://www.durhamclimbingcentre.co.uk/coaching"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def search_tags(tag):
    searched_soup = soup.find_all(tag)
    tag_list = [e.string for e in searched_soup]
    return tag_list


def remove_blanks(list):
    new_list = []
    for i in list:
        if i != None:
            new_list.append(i)
    return new_list


def do_join(list):
    new_list = []
    for j in list:
        j = " ".join(j.split())
        new_list.append(j)
    return new_list


def find_p():
    """search the html for <p> tags and return the content as a list"""
    p_tags = []
    p_tag_list = soup.find_all('p')
    for e in p_tag_list:
        e = e.text
        p_tags.append(e)
    return p_tags


def display_class_text(list):
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

    class_list = list
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.executemany(
        'INSERT OR REPLACE INTO centres (name, url) VALUES (:name, :url);', class_list)
    cur.executemany(
        'INSERT or replace INTO classes (url, title, description) VALUES (:url, :title, :description);', class_list)
    conn.commit()
    print("Records successfully added")
    # conn.close()

    conn = sqlite3.connect('database.db')
    data = conn.execute(
        "SELECT * FROM classes LEFT JOIN centres USING (url);")

    name = ''
    url = ''
    title = ''
    description = []
    # list_of_classes = []

    for row in data:
        if row[3] != name:
            name = (f'{row[3]}')
            # list_of_classes.append(f'\n\n{name}')
            print(f'\n{name}')

        if row[0] != url:
            url = row[0]
            # list_of_classes.append(url)
            print(url)

        if row[1] != title:
            title = (row[1])
            # list_of_classes.append(f'\n{title}')
            print(f'\n{title}')

        description.append(row[2])
        for d in description:
            # list_of_classes.append(d)
            print(d)
            description = []
            continue


h2_tags = search_tags('h2')
h2_tags = do_join(h2_tags)


h3_tags = search_tags('h3')
h3_tags = remove_blanks(h3_tags)
h3_tags = do_join(h3_tags)

span_tags = search_tags('span')
span_tags = remove_blanks(span_tags)

li_tags = search_tags('li')
li_tags = remove_blanks(li_tags)

div_tags = []
div_tag_list = search_tags('div')
for i in div_tag_list:
    if i != None and "\xa0" not in i and "Contact Us" not in i and "Stay tuned" not in i:
        div_tags.append(i)
div_tags = do_join(div_tags)

p_tags = find_p()


class_list = [
    {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h3_tags[0],
        "description": div_tags[0]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h3_tags[0],
        "description": p_tags[0]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[0],
        "description": p_tags[1]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[0],
        "description": p_tags[2]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[0],
        "description": p_tags[3]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[1],
        "description": div_tags[10]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[1],
        "description": p_tags[5]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h3_tags[1],
        "description": div_tags[11]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h3_tags[1],
        "description": p_tags[6]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h3_tags[1],
        "description": p_tags[7]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[2],
        "description": div_tags[12]
    }, {
        "name": "Durham Climbing Centre, Durham",
        "url": url,
        "title": h2_tags[2],
        "description": p_tags[8]
    }
]

display_class_text(class_list)
'''
"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(durham_classes, file, indent=4)
'''
'''def find_h2():
    """search the html for <h4> tags and return the content as a list"""
    list_1 = []
    h2_tag = soup.find_all('h2')
    h2_tag_list = [e.string for e in h2_tag]
    for t in h2_tag_list:
        t = " ".join(t.split())
        list_1.append(t)
    return list_1

def find_h3():
    """search the html for <h3> tags and return the content as a list"""
    list_1 = []
    list_2 = []
    h3_tag = soup.find_all('h3')
    h3_tag_list = [e.string for e in h3_tag]
    for p in h3_tag_list:
        if p != None:
            list_1.append(p)
    for t in list_1:
        t = " ".join(t.split())
        list_2.append(t)
    return list_2
    
    def find_div():
    """search the html for <div> tags and return the content as a list"""
    list_1 = []
    list_2 = []
    div_tag = soup.find_all('div')
    div_tag_list = [e.string for e in div_tag]
    for p in div_tag_list:
        if p != None and "\xa0" not in p and "Contact Us" not in p and "Stay tuned" not in p:
            list_1.append(p)
    for t in list_1:
        t = " ".join(t.split())
        list_2.append(t)
    return list_2
    
    def find_span():
    """search the html for <span> tags and return the content as a list"""
    list_1 = []
    span_tag = soup.find_all('span')
    span_tag_list = [e.string for e in span_tag]
    for p in span_tag_list:
        if p != None:
            list_1.append(p)
    return list_1
    
    def find_li():
    """search the html for <li> tags and return the content as a list"""
    list_1 = []
    li_tag = soup.find_all('li')
    li_tag_list = [e.string for e in li_tag]
    for p in li_tag_list:
        if p != None:
            list_1.append(p)
    return list_1
    
    



find_h1 = find_h1()
find_h2 = find_h2()
find_h3 = find_h3()
find_div = find_div()
find_p = find_p()
find_span = find_span()
find_li = find_li()'''
