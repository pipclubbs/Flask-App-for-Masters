"""module containing the class that scrapes websites for climbing club data (Yorkshire)"""
import datetime
import db_conn
from class_scrapers import ClassScraper


class YorkshireClubs(ClassScraper):
    """class containing the web scraping information for climbing clubs (Yorkshire)"""
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
                "area": "yorkshire",
                "name": "Harrogate Mountaineering Club",
                "url": "https://harrogatemc.wordpress.com/about-2/"
            }, {
                "type": "club",
                "area": "yorkshire",
                "name": "Leeds Mountaineering Club",
                "url": "https://www.leedsmc.org/"
            }, {
                "type": "club",
                "area": "yorkshire",
                "name": "York Alpine Club",
                "url": "http://www.yorkalpineclub.org.uk/"
            }
        ]

        for c in clubs:
            if c["name"] == "Harrogate Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url) # get html via parent class

                if soup:
                    # search for the tags in the html
                    p_tags = self.search_tags_alternative('p', soup)

                    # allocate the results to a dictionary for storing in the database
                    club_list = [
                        {
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
                        }
                    ]
                    # append the dictionaries to a list
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "Leeds Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    p_tags = self.search_tags_alternative('p', soup)
                    p_tag_list = []
                    for tag in p_tags:
                        p_tag_list.append(tag.replace("\n\t\t\t\t\t\t", ""))

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[0],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[1],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[2],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[3],
                            "created": created
                        }, {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[4],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

            if c["name"] == "York Alpine Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                if soup:
                    p_tags = self.search_tags('p', soup)
                    p_tags = self.remove_blanks(p_tags)
                    p_tags = self.strip_spaces_and_breaks(p_tags)

                    td_tags = self.search_tags_alternative('td', soup)
                    td_tags = self.strip_spaces_and_breaks(td_tags)

                    li_tags = self.search_tags('li', soup)
                    li_tags = self.strip_spaces_and_breaks(li_tags)

                    club_list = [
                        {
                            "type": "club",
                            "area": area,
                            "name": c["name"],
                            "url": url,
                            "intro": td_tags[2],
                            "title": '',
                            "subtitle": '',
                            "description": td_tags[3],
                            "created": created
                        }
                    ]
                    for i in club_list:
                        scraped_clubs.append(i)

                else:
                    pass

        """send the compiled club list to the database module, and 
        append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output
