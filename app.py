from flask import Flask, request, render_template, redirect
from class_scrapers import ClassScraper
from northeast_classes import NorthEastClasses
from yorkshire_classes import YorkshireClasses
from midlands_classes import MidlandsClasses
from northwest_classes import NorthWestClasses
from northwest_contacts import NorthWestContacts
from northeast_contacts import NorthEastContacts
from midlands_contacts import MidlandsContacts
from yorkshire_contacts import YorkshireContacts
from northeast_clubs import NorthEastClubs
from northwest_clubs import NorthWestClubs
from midlands_clubs import MidlandsClubs
from yorkshire_clubs import YorkshireClubs
<<<<<<< Updated upstream
# from db_conn2 import DatabaseConnection
=======
from events import Events
>>>>>>> Stashed changes

import sqlite3
import os

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


@app.route('/walls', methods=['GET', 'POST'])
def climb_walls():
    """the page where the information for the climbing walls will display after scraping"""
    wall_search = ''
    if request.method == "POST" and "wallsearch" in request.form:
        wall_search = request.form.get('wallsearch')
        if wall_search == "north-west":
            check = centre_data_exists("north-west")
            print(f'this is where the final outcome is: {check}')
            if not check:
                search = NorthWestContacts()
                search.assign_values()
                return display_centre_text("north-west")
            else:
                return display_centre_text("north-west")
        elif wall_search == "north-east":
            check = centre_data_exists("north-east")
            if not check:
                search = NorthEastContacts()
                search.assign_values()
                return display_centre_text("north-east")
            else:
                return display_centre_text("north-east")
        elif wall_search == "midlands":
            check = centre_data_exists("midlands")
            if not check:
                search = MidlandsContacts()
                search.assign_values()
                return display_centre_text("midlands")
            else:
                return display_centre_text("midlands")
        elif wall_search == "yorkshire":
            check = centre_data_exists("yorkshire")
            if not check:
                search = YorkshireContacts()
                search.assign_values()
                return display_centre_text("yorkshire")
            else:
                return display_centre_text("yorkshire")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()


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


@app.route('/events', methods=['GET', 'POST'])
def climb_events():
    """the page where the information for climbing events will display after scraping"""
    event_search = ''
    if request.method == "POST" and "eventsearch" in request.form:
        event_search = request.form.get('eventsearch')

        # return render_template("events.jinja2", event_search=event_search)

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("events.jinja2", event_search=event_search)


@app.route('/clubs', methods=['GET', 'POST'])
def climb_clubs():
    """the page where the information for climbing clubs will display after scraping"""
    club_search = ''
    if request.method == "POST" and "clubsearch" in request.form:
        club_search = request.form.get('clubsearch')
        if club_search == "north-east":
            list_of_clubs = NorthEastClubs()
            list_of_clubs.assign_values()
            return display_club_text("north-east")
        elif club_search == "north-west":
            list_of_clubs = NorthWestClubs()
            list_of_clubs.assign_values()
            return display_club_text("north-west")
        elif club_search == "midlands":
            list_of_clubs = MidlandsClubs()
            list_of_clubs.assign_values()
            return display_club_text("midlands")
        elif club_search == "yorkshire":
            list_of_clubs = YorkshireClubs()
            list_of_clubs.assign_values()
            return display_club_text("yorkshire")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("clubs.jinja2", club_search=club_search)


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

    for row in data:
        if row[0] != name:
            name = (f'{row[0]}')
            list_of_classes.append(f'\n\n{name}')

        if row[1] != url:
            url = row[1]
            list_of_classes.append(url)

        if row[2] != title:
            title = (row[2])
            list_of_classes.append(f'\n{title}')

        description.append(row[3])
        for d in description:
            list_of_classes.append(d)
            description = []
            continue

    conn.close()
    return render_template("classes.jinja2", class_search=list_of_classes)


def display_centre_text(area):
    area = area
    print(f'FINAL AREA: {area}')
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM centres WHERE area = ?;"
    data = conn.execute(query, (area,))

    # for row in data:
    #    print(row)
    list_of_centres = []
    # for row in data:
    #    print(row)#
    for row in data:
        if row[0] == area and row[2] is not None:
            list_of_centres.append(f'\n\n{row[1]}')
            list_of_centres.append(row[5])
            list_of_centres.append(row[6])
            list_of_centres.append(row[7])
            list_of_centres.append(row[8])
            list_of_centres.append(row[9])
            list_of_centres.append(row[10])
            list_of_centres.append(f'{row[2]}')
    print(list_of_centres)
    conn.close()
    return render_template("walls.jinja2", wall_search=list_of_centres)


def display_club_text(area):
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM clubs WHERE area = ?;"
    data = conn.execute(query, (area,))

    name = ''
    url = ''
    intro = ''
    title = ''
    subtitle = ''
    description = []
    list_of_clubs = []

    for row in data:
        if row[1] != name:
            name = (f'{row[1]}')
            list_of_clubs.append(f'\n\n{name}')

        if row[2] != url:
            url = row[2]
            list_of_clubs.append(url)

        if row[3] != intro:
            intro = (row[3])
            list_of_clubs.append(f'{intro}')

        if row[4] != title:
            title = (row[4])
            list_of_clubs.append(f'\n{title}')

        if row[5] != subtitle:
            subtitle = (row[5])
            list_of_clubs.append(f'\n{subtitle}')

        description.append(row[6])
        for d in description:
            list_of_clubs.append(d)
            description = []
            continue

    conn.close()
    return render_template("clubs.jinja2", class_search=list_of_clubs)


def check_class_table(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM classes WHERE area = ?", (searched_area,))
    find = cur.fetchall()

    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)

    if found_rows:
        return True
    else:
        return False


def check_centre_table(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    print(f'searched_area in check centre data = {searched_area}')
    cur.execute(
        "SELECT * FROM centres WHERE area = ? ", (searched_area,))
    find = cur.fetchall()
    print(f'find: {find}')

    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)
        print(f'found_rows in check data centre: {found_rows}')

    if found_rows:
        return True
    else:
        return False


def check_rows_for_info(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print(f'searched_area: {searched_area}')

    cur.execute("SELECT * FROM centres WHERE area = ? ",
                (searched_area,))
    find = cur.fetchall()

    print(f'find:{find}')

    found_rows = []
    for row in find:
        print(f'check rows found rows: {row}')
        if row[2] != None:
            found_rows.append(row)

    if found_rows:
        return True
    else:
        return False

        # returns true is any are true


def centre_data_exists(area):
    search_area = area
    if not os.path.isfile('database.db'):
        return False

    else:
        check_centres = check_centre_table(search_area)
        if check_centres:
            check_2 = check_rows_for_info(search_area)
            if check_2:  # if this is true, then there is full centre data
                return True
            else:
                return False
        else:
            return False


'''def data_exists(area):
    search_area = area
    if not os.path.isfile('database.db'):
        return False

    else:
        check_classes = check_class_table(search_area)
        if check_classes:
            checked_classes = True
        else:
            checked_classes = False

        check_centres = check_centre_table(search_area)
        if check_centres:
            check_2 = check_rows_for_info(search_area)
            if check_2:  # if this is true, then there is full centre data
                checked_centres = True
            else:
                checked_centres = False

        return checked_centres, checked_classes'''


returnHome = returnHome()

app.run()
