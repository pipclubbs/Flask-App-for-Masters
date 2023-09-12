from flask import Flask, request, render_template, redirect

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

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("walls.html", wall_search=wall_search)

    # need to add in information here for parsing the information in from the scraper


@app.route('/classes', methods=['GET', 'POST'])
def climb_classes():
    """the page where the information for climbing classes will display after scraping"""
    class_search = ''
    if request.method == "POST" and "classsearch" in request.form:
        class_search = request.form.get('classsearch')
    # need to add something to instruct the scrapers for each area to go

    if request.method == "GET" and "home" in request.form:
        return returnHome()

    if request.method == "GET" and "about-me" in request.form:
        return returnAboutMe()

    return render_template("classes.html", class_search=class_search)
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


returnHome = returnHome()


app.run()
