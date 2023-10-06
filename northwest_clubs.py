"""module containing the class that scrapes websites for climbing club data (North West)"""
import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthWestClubs(ClassScraper):
    """class containing the web scraping information for climbing clubs (North West)"""
    def __init__(self):
        super().__init__()


    """method that defines the sites to scrape, then runs through each in turn and sorts the results
    into dictionaries ready for storing in the database"""
    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        scraped_clubs = []
        clubs = [
            {
                "type": "club",
                "area": "north-west",
                "name": "West Cumbria Mountaineering Club",
                "url": "https://www.westcumbriamountaineeringclub.co.uk/"
            }, {
                "type": "club",
                "area": "north-west",
                "name": "Kendal Mountaineering Club",
                "url": "https://kendalmc.org/about-the-club/"
            }, {
                "type": "club",
                "area": "north-west",
                "name": "The Wayfarer's Club",
                "url": "http://www.wayfarersclub.org.uk/"
            }
        ]

        for c in clubs:
            if c["name"] == "West Cumbria Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url) # get the html via the parent class

                if soup:
                    # search for the tags in the html
                    span_tags = self.search_tags('span', soup)
                    p_tags = self.search_tags_alternative('p', soup)

                    # allocate the results to a dictionary for storing in the database
                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": f'{span_tags[0]}{span_tags[1]}',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[0],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
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
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "Kendal Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    h2_tags = self.search_tags_alternative('h2', soup)
                    p_tags = self.search_tags_alternative('p', soup)

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[0],
                            "subtitle": '',
                            "description": p_tags[1],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[0],
                            "subtitle": '',
                            "description": p_tags[2],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[1],
                            "subtitle": '',
                            "description": p_tags[5],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[1],
                            "subtitle": '',
                            "description": p_tags[6],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[1],
                            "subtitle": '',
                            "description": p_tags[7],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[1],
                            "subtitle": '',
                            "description": p_tags[8],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[2],
                            "subtitle": '',
                            "description": p_tags[9],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[2],
                            "subtitle": '',
                            "description": p_tags[10],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[2],
                            "subtitle": '',
                            "description": p_tags[11],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "The Wayfarer's Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    p_tags = self.search_tags('p', soup)
                    h2_tags = self.search_tags('h2', soup)

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": h2_tags[0],
                            "subtitle": '',
                            "description": p_tags[8],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[9],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[10],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tags[11],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

        """send the compiled club list to the database module,
        and append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output
