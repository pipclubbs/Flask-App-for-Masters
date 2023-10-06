"""this is the main application page that controls the homepage
and menu choices"""
import sqlite3
import os
import datetime
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
        check_age_of_data() # run function to check how old database data is

        if wall_search == "north-west":
            check = centre_data_exists("north-west") # check the database exists
            if not check:
                search = NorthWestContacts()  # create a scraper instance
                search.assign_values()  # run the scraper using the class method
                return display_centre_text("north-west") # open the results page
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
        check_age_of_data()

        if class_search == "north-east":
            check = class_data_exists("north-east")
            if not check:
                list_of_classes = NorthEastClasses()
                list_of_classes.assign_values()
                return display_class_text("north-east")
            return display_class_text("north-east")

        if class_search == "yorkshire":
            check = class_data_exists("yorkshire")
            if not check:
                list_of_classes = YorkshireClasses()
                list_of_classes.assign_values()
                return display_class_text("yorkshire")
            return display_class_text("yorkshire")

        if class_search == "midlands":
            check = class_data_exists("midlands")
            if not check:
                list_of_classes = MidlandsClasses()
                list_of_classes.assign_values()
                return display_class_text("midlands")
            return display_class_text("midlands")

        if class_search == "north-west":
            check = class_data_exists("north-west")
            if not check:
                list_of_classes = NorthWestClasses()
                list_of_classes.assign_values()
                return display_class_text("north-west")
            return display_class_text("north-west")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()


@app.route('/events', methods=['GET', 'POST'])
def climb_events():
    """the page where the information for climbing events will display after scraping"""
    if request.method == "POST" and "eventsearch" in request.form:
        check_age_of_data()
        
        check = event_data_exists()
        if not check:
            list_of_events = Events()
            list_of_events.assign_values()
            print("this worked")
            return display_event_text()
        return display_event_text()

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    
@app.route('/clubs', methods=['GET', 'POST'])
def climb_clubs():
    """the page where the information for climbing clubs will display after scraping"""
    club_search = ''
    if request.method == "POST" and "clubsearch" in request.form:
        club_search = request.form.get('clubsearch')
        check_age_of_data()

        if club_search == "north-east":
            check = club_data_exists("north-east")
            if not check:
                list_of_clubs = NorthEastClubs()
                list_of_clubs.assign_values()
                return display_club_text("north-east")
            return display_club_text("north-east")

        if club_search == "north-west":
            check = club_data_exists("north-west")
            if not check:
                list_of_clubs = NorthWestClubs()
                list_of_clubs.assign_values()
                return display_club_text("north-west")
            return display_club_text("north-west")

        if club_search == "midlands":
            check = club_data_exists("midlands")
            if not check:
                list_of_clubs = MidlandsClubs()
                list_of_clubs.assign_values()
                return display_club_text("midlands")
            return display_club_text("midlands")

        if club_search == "yorkshire":
            check = club_data_exists("yorkshire")
            if not check:
                list_of_clubs = YorkshireClubs()
                list_of_clubs.assign_values()
                return display_club_text("yorkshire")
            return display_club_text("yorkshire")

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()


@app.route('/about')
def about_me():
    """A page with general information on me and the app, perhaps with blog-type functionality"""
    if request.method == "GET" and "home" in request.form:
        return returnHome()

    return render_template("about.html")

"""method to check that the table exists in the database"""
def table_exists(cursor, table_name):
    cur = cursor
    cur.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cur.fetchone() is not None

"""method to check how that there is a database, and if so, how old the data is. 
if it is more than 24 hours old, delete it"""
def check_age_of_data():
    if not os.path.isfile('database.db'):
        pass

    else:
        max_time = datetime.datetime.now() - datetime.timedelta(hours=24)
        print(f'max time: {max_time}')
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        if table_exists(cur, 'centres'):
            cur.execute(
                "DELETE FROM centres WHERE created < ?", (max_time,))

        if table_exists(cur, 'classes'):
            cur.execute(
                "DELETE FROM classes WHERE created < ?", (max_time,))

        if table_exists(cur, 'clubs'):
            cur.execute(
                "DELETE FROM clubs WHERE created < ?", (max_time,))

        if table_exists(cur, 'events'):
            cur.execute(
                "DELETE FROM events WHERE created < ?", (max_time,))

        conn.commit()
        print("old data has been deleted from the tables")
        conn.close()


"""method to pull the data from the class table and save it in
a list for the jinja2 template to use"""
def display_class_text(area):
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


"""method to pull the data from the centre table and save it in
a list for the jinja2 template to use"""
def display_centre_text(area):
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


"""method to pull the data from the clubs table and save it in
a list for the jinja2 template to use"""
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


"""method to pull the data from the events table and save it in
a list for the jinja2 template to use"""
def display_event_text():
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
        # (f'display event text: {row}')
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


"""method to check whether database file exists, and if so check whether 
rows exist in the class table for the selected area"""
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
    return False


"""method to check whether database file exists, and if so check whether 
rows exist in the centre table for the selected area"""
def check_centre_table(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM centres WHERE area = ? ", (searched_area,))
    find = cur.fetchall()
    
    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)

    if found_rows:
        return True
    return False


"""method to check whether database file exists, and if so check whether 
rows exist in the class table for the selected area"""
def check_club_table(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM clubs WHERE area = ?", (searched_area,))
    find = cur.fetchall()

    found_rows = []
    for row in find:
        if row[0] == searched_area:
            found_rows.append(row)

    if found_rows:
        return True
    return False


"""method to check whether there are rows in the events
table"""
def check_event_table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM events")
    find = cur.fetchall()

    if find:
        return True
    return False


"""method to open the database and search for the search area inside 
it. if it is there, it returns True"""
def check_rows_for_info(area):
    searched_area = area
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
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


"""method to check if the database file exists"""
def centre_data_exists(area):
    search_area = area
    if not os.path.isfile('database.db'):
        return False

    check_centres = check_centre_table(search_area)
    if check_centres:
        check_2 = check_rows_for_info(search_area)
        if check_2:  # if this is true, then there is full centre data
            return True
        return False
    return False


"""method to check if the database exists, and if so run the class table check
- no need to check if the centre table exists because the data needed in there 
would only exist if the class rows exist"""
def class_data_exists(area):
    search_area = area
    if not os.path.isfile('database.db'):
        return False
    return check_class_table(search_area)


"""method to check the database exists, then run the club table check"""
def club_data_exists(area):
    search_area = area
    if not os.path.isfile('database.db'):
        return False
    return check_club_table(search_area)


"""method to check the database exists, then run the event table check"""
def event_data_exists():
    if not os.path.isfile('database.db'):
        return False
    return check_event_table()


returnHome = returnHome()

if __name__ == "__main__":
    app.run()
