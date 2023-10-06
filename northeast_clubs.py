"""module containing the class that scrapes websites for climbing club data (North East)"""
import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthEastClubs(ClassScraper):
    """class containing the web scraping information for climbing clubs (North East)"""
    def __init__(self):
        super().__init__()
        

    """method that defines the sites to scrape, then runs through each in turn and sorts the
    results into dictionaries ready for storing in the database"""
    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        scraped_clubs = []
        clubs = [
            {
                "type": "club",
                "area": "north-east",
                "name": "Northumbrian Mountaineering Club",
                "url": "https://thenmc.org.uk"
            }, {
                "type": "club",
                "area": "north-east",
                "name": "Sunderland Mountaineering Club",
                "url": "https://www.sunderlandmc.co.uk/climbing"
            }, {
                "type": "club",
                "area": "north-east",
                "name": "Durham Mountain Sports",
                "url": "https://durhammountainsports.org.uk/wp/about/"
            }
        ]

        for c in clubs:
            if c["name"] == "Northumbrian Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url) # get the html via the parent class method

                if soup:
                    # search for the tags in the html
                    h4_tags = self.search_tags('h4', soup)
                    p_tags = self.search_tags('p', soup)

                    # allocate the results to a dictionary for storing in the database
                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": h4_tags[1],  # the club caters for
                            "title": h4_tags[2],  # a little bit...
                            "subtitle": h4_tags[3],  # social
                            "description": p_tags[2],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": h4_tags[1],  # the club caters for
                            "title": h4_tags[2],  # a little bit...
                            "subtitle": h4_tags[4],  # experienced
                            "description": p_tags[3],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": h4_tags[1],  # the club caters for
                            "title": h4_tags[2],  # a little bit...
                            "subtitle": h4_tags[5],  # active
                            "description": p_tags[4],
                            "created": created
                        }
                    ]
                    # add each dictionary entry to a list
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "Sunderland Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    span_tags = self.search_tags_alternative('span', soup)

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": span_tags[2],  # climbing
                            "subtitle": '',
                            "description": span_tags[4],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": span_tags[2],  # climbing
                            "subtitle": '',
                            "description": span_tags[5],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": span_tags[2],  # climbing
                            "subtitle": '',
                            "description": span_tags[6],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "Durham Mountain Sports":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    p_tags = self.search_tags_alternative('p', soup)

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": p_tags[0],
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[1],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[2],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[3],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[4],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[5],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

        """send the compiled scraped club list to the database module, 
        and append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output
