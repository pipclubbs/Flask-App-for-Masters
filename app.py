from flask import Flask, request, render_template, redirect
from class_scrapers import ClassScraper
from northeast_classes import NorthEastClasses
from yorkshire_classes import YorkshireClasses
from midlands_classes import MidlandsClasses
from northwest_classes import NorthWestClasses
from northwest_contacts import NorthWestContacts

import sqlite3

app = Flask(__name__)


def returnHome():
    return redirect('/')


def returnAboutMe():
    return redirect('/about')


@app.route('/', methods=['GET', 'POST'])
def climb_home():
    """home page for the scraper"""

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("index.html")
    # need to add code here for where the user would type in their queries


@app.route('/walls', methods=['GET', 'POST'])
def climb_walls():
    """the page where the information for the climbing walls will display after scraping"""
    wall_search = ''
    if request.method == "POST" and "wallsearch" in request.form:
        wall_search = request.form.get('wallsearch')
        if wall_search == "north-west":
            search = NorthWestContacts()
            search.assign_values()
            return display_centre_text()

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    # return render_template("walls.html", wall_search=wall_search)

    # need to add in information here for parsing the information in from the scraper


@app.route('/classes', methods=['GET', 'POST'])
def climb_classes():
    """the page where the information for climbing classes will display after scraping"""
    # output = []
    class_search = ''
    list_of_classes = ''
    if request.method == "POST" and "classsearch" in request.form:
        class_search = request.form.get('classsearch')
    # need to add something to instruct the scrapers for each area to go
        if class_search == "north-east":
            list_of_classes = NorthEastClasses()
            list_of_classes.assign_values()
            return display_class_text("north-east")

        elif class_search == "yorkshire":
            list_of_classes = YorkshireClasses()
            list_of_classes.assign_values()
            return display_class_text("yorkshire")

        elif class_search == "midlands":
            list_of_classes = MidlandsClasses()
            list_of_classes.assign_values()
            return display_class_text("midlands")

        elif class_search == "north-west":
            list_of_classes = NorthWestClasses()
            list_of_classes.assign_values()
            return display_class_text("north-west")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    # need to add in information here for parsing the information in from the scrape


@app.route('/events', methods=['GET', 'POST'])
def climb_events():
    """the page where the information for climbing events will display after scraping"""
    event_search = ''
    if request.method == "POST" and "eventsearch" in request.form:
        event_search = request.form.get('eventsearch')

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("events.html", event_search=event_search)
    # need to add in information here for parsing the information in from the scraper


@app.route('/clubs', methods=['GET', 'POST'])
def climb_clubs():
    """the page where the information for climbing clubs will display after scraping"""
    club_search = ''
    if request.method == "POST" and "clubsearch" in request.form:
        club_search = request.form.get('clubsearch')

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("clubs.html", club_search=club_search)
    # need to add in information here for parsing the information in from the scraper


@app.route('/about')
def about_me():
    """A page with general information on me and the app, perhaps with blog-type functionality"""
    if request.method == "GET" and "home" in request.form:
        return returnHome()

    return render_template("about.html")
    # need to think about whether to add something in here


def display_class_text(area):
    # list_of_classes = list.assign_values()
    area = area
    conn = sqlite3.connect('database.db')
    query = '''
        SELECT name, classUrl, title, description 
        FROM classes
        LEFT JOIN centres USING (classUrl)
        WHERE classes.area = ?
    '''
    data = conn.execute(query, (area,))

    name = ''
    url = ''
    title = ''
    description = []
    list_of_classes = []

    # for row in data:
    #    print(row)
    for row in data:
        if row[0] != name:
            name = (f'{row[0]}')
            list_of_classes.append(f'\n\n{name}')
            # print(f'\n{name}')

        if row[1] != url:
            url = row[1]
            list_of_classes.append(url)
            # print(url)

        if row[2] != title:
            title = (row[2])
            list_of_classes.append(f'\n{title}')
            # print(f'\n{title}')

        description.append(row[3])
        for d in description:
            list_of_classes.append(d)
            # print(d)
            description = []
            continue

    conn.close()
    return render_template("classes.html", class_search=list_of_classes)


def display_centre_text():
    conn = sqlite3.connect('database.db')
    data = conn.execute(
        "SELECT * FROM centres;")

    list_of_centres = []

    for row in data:
        # print(row)
        if row[0] == "north-west":
            list_of_centres.append(f'\n\n{row[1]}')
            list_of_centres.append(row[5])
            list_of_centres.append(row[6])
            list_of_centres.append(row[7])
            list_of_centres.append(row[8])
            list_of_centres.append(row[9])
            list_of_centres.append(row[10])
            list_of_centres.append(row[2])

    conn.close()
    # print(list_of_centres)
    return render_template("walls.html", wall_search=list_of_centres)


returnHome = returnHome()


app.run()
