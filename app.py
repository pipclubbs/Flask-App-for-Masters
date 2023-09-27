"""this is the main application page that controls the homepage
and menu choices"""
import sqlite3
import os

from flask import Flask, request, render_template, redirect

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
from events import Events

app = Flask(__name__)


def returnHome():
    return redirect('/')


def returnAboutMe():
    return redirect('/about')


@app.route('/', methods=['GET', 'POST'])
def climb_home():
    """home page for the scraper"""
    # if user clicks the 'About Me' button, return the page
    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()
    # else, return the home page
    return render_template("index.html")


@app.route('/walls', methods=['GET', 'POST'])
def climb_walls():
    """builds the page where the information for the climbing walls 
    will display after scraping"""
    wall_search = ''
    # if user uses the search for climbing walls
    if request.method == "POST" and "wallsearch" in request.form:
        wall_search = request.form.get('wallsearch')

        if wall_search == "north-west":
            # check the database exists
            check = centre_data_exists("north-west")
            if not check:
                # if doesn't...
                search = NorthWestContacts()  # create a scraper instance
                search.assign_values()  # run the scraper using the class method
                # open the results page
                return display_centre_text("north-west")
            # if it does, open the result page
            return display_centre_text("north-west")

        if wall_search == "north-east":
            check = centre_data_exists("north-east")
            if not check:
                search = NorthEastContacts()
                search.assign_values()
                return display_centre_text("north-east")
            return display_centre_text("north-east")

        if wall_search == "midlands":
            check = centre_data_exists("midlands")
            if not check:
                search = MidlandsContacts()
                search.assign_values()
                return display_centre_text("midlands")
            return display_centre_text("midlands")

        if wall_search == "yorkshire":
            check = centre_data_exists("yorkshire")
            if not check:
                search = YorkshireContacts()
                search.assign_values()
                return display_centre_text("yorkshire")
            return display_centre_text("yorkshire")

    if request.method == "GET" and "home" in request.form:
        return returnHome()  # if user selects home button, return home

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()  # if user selects about me, open that page

    # add an error page?


@app.route('/classes', methods=['GET', 'POST'])
def climb_classes():
    """the page where the information for climbing classes will display after scraping"""
    class_search = ''
    list_of_classes = ''
    if request.method == "POST" and "classsearch" in request.form:
        class_search = request.form.get('classsearch')
    # need to add database checks
        if class_search == "north-east":
            list_of_classes = NorthEastClasses()
            list_of_classes.assign_values()
            return display_class_text("north-east")

        if class_search == "yorkshire":
            list_of_classes = YorkshireClasses()
            list_of_classes.assign_values()
            return display_class_text("yorkshire")

        if class_search == "midlands":
            list_of_classes = MidlandsClasses()
            list_of_classes.assign_values()
            return display_class_text("midlands")

        if class_search == "north-west":
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
    if request.method == "POST" and "eventsearch" in request.form:
        check = event_data_exists()
        if not check:
            list_of_events = Events()
            list_of_events.assign_values()
            return display_event_text()
        else:
            return display_event_text()

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    # return render_template("events.jinja2", event_search=event_search)


@app.route('/clubs', methods=['GET', 'POST'])
def climb_clubs():
    """the page where the information for climbing clubs will display after scraping"""
    club_search = ''
    if request.method == "POST" and "clubsearch" in request.form:
        club_search = request.form.get('clubsearch')
        if club_search == "north-east":
            check = club_data_exists("north-east")
            if not check:
                list_of_clubs = NorthEastClubs()
                list_of_clubs.assign_values()
                return display_club_text("north-east")
            else:
                return display_club_text("north-east")
        elif club_search == "north-west":
            check = club_data_exists("north-west")
            if not check:
                list_of_clubs = NorthWestClubs()
                list_of_clubs.assign_values()
                return display_club_text("north-west")
            else:
                return display_club_text("north-west")
        elif club_search == "midlands":
            check = club_data_exists("midlands")
            if not check:
                list_of_clubs = MidlandsClubs()
                list_of_clubs.assign_values()
                return display_club_text("midlands")
            else:
                return display_club_text("midlands")
        elif club_search == "yorkshire":
            check = club_data_exists("yorkshire")
            if not check:
                list_of_clubs = YorkshireClubs()
                list_of_clubs.assign_values()
                return display_club_text("yorkshire")
            else:
                return display_club_text("yorkshire")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    #


@app.route('/about')
def about_me():
    """A page with general information on me and the app, perhaps with blog-type functionality"""
    if request.method == "GET" and "home" in request.form:
        return returnHome()

    return render_template("about.html")


def display_class_text(area):
    """this method pulls the data from the class table and saves it in
    a list for the jinja2 template to use"""
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
            name = f'{row[0]}'
            list_of_classes.append(f'\n\n{name}')

        if row[1] != url:
            url = row[1]
            list_of_classes.append(url)

        if row[2] != title:
            title = row[2]
            list_of_classes.append(f'\n{title}')

        description.append(row[3])
        for d in description:
            list_of_classes.append(d)
            description = []
            continue

    conn.close()
    return render_template("classes.jinja2", class_search=list_of_classes)


def display_centre_text(area):
    """this method pulls the data from the centre table and saves it in
    a list for the jinja2 template to use"""
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM centres WHERE area = ?;"
    data = conn.execute(query, (area,))

    list_of_centres = []
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

    conn.close()
    return render_template("walls.jinja2", wall_search=list_of_centres)


def display_club_text(area):
    """this method pulls the data from the clubs table and saves it in
    a list for the jinja2 template to use"""
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
            intro = row[3]
            list_of_clubs.append(f'{intro}')

        if row[4] != title:
            title = row[4]
            list_of_clubs.append(f'\n{title}')

        if row[5] != subtitle:
            subtitle = row[5]
            list_of_clubs.append(f'\n{subtitle}')

        description.append(row[6])
        for d in description:
            list_of_clubs.append(d)
            description = []
            continue

    conn.close()
    return render_template("clubs.jinja2", class_search=list_of_clubs)


def display_event_text():
    """this method pulls the data from the events table and saves it in
    a list for the jinja2 template to use"""
    conn = sqlite3.connect('database.db')
    data = conn.execute("SELECT * FROM events;")

    name = ''
    url = ''
    intro = ''
    title = ''
    subtitle = ''
    description = []
    list_of_events = []

    for row in data:
        print(f'display event text: {row}')
        if row[0] != name:
            name = row[0]
            list_of_events.append(f'\n\n{row[0]}')

        if row[1] != url:
            url = row[1]
            list_of_events.append(url)

        if row[2] != intro:
            intro = row[2]
            list_of_events.append(row[2])

        if row[3] != title:
            title = row[3]
            list_of_events.append(f'\n{row[3]}')

        if row[4] != subtitle:
            subtitle = row[4]
            list_of_events.append(f'\n{row[4]}')

        description.append(row[5])
        for d in description:
            list_of_events.append(d)
            description = []
            continue

    conn.close()
    return render_template("events.jinja2", event_search=list_of_events)


def check_class_table(area):
    """check whether database file exists, if so check whether rows 
    exist in the class table for the selected area"""
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
    return False


def check_centre_table(area):
    """check whether database file exists, if so check whether rows 
    exist in the centre table for the selected area"""
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # print(f'searched_area in check centre data = {searched_area}')
    cur.execute(
        "SELECT * FROM centres WHERE area = ? ", (searched_area,))
    find = cur.fetchall()
    # print(f'find: {find}')

    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)
        # print(f'found_rows in check data centre: {found_rows}')

    if found_rows:
        return True
    return False


def check_clubs_table(area):
    """check whether there is data for the searched area in the table"""
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM clubs WHERE area = ? ", (searched_area,))
    find = cur.fetchall()

    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)

    if found_rows:
        return True
    return False


def check_events_table():
    """check whether there is data in the events table"""
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM events;")
    find = cur.fetchall()

    found_rows = []
    for row in find:
        if row:
            found_rows.append(row)

    if found_rows:
        return True
    return False


def check_rows_for_info(area):
    """opens the database and searches for the search area inside it
    if it is there, it returns True"""
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print(f'searched_area: {searched_area}')

    cur.execute("SELECT * FROM centres WHERE area = ? ",
                (searched_area,))
    find = cur.fetchall()

    found_rows = []
    for row in find:
        if row[2] is not None:
            found_rows.append(row)

    if found_rows:
        return True
    return False


def centre_data_exists(area):
    """checks if the database file exists"""
    search_area = area
    if not os.path.isfile('database.db'):
        return False
    # if it does, check for the search area in the rows
    check_centres = check_centre_table(search_area)
    # if they're there, do a more indepth check to see what data is there
    if check_centres:
        check_2 = check_rows_for_info(search_area)
        if check_2:  # if this is true, then there is full centre data
            return True
        return False
    return False


def club_data_exists(area):
    """check if the database file exists"""
    search_area = area
    if not os.path.isfile('database.db'):
        return False
    # if it does, check for the search area in the rows
    check_clubs = check_clubs_table(search_area)
    if check_clubs:
        return True
    return False


def event_data_exists():
    """check if the database file exists"""
    if not os.path.isfile('database.db'):
        return False
    # if it does, check there are entries in the table
    check_events = check_events_table()
    if check_events:
        return True
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
