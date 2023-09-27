import datetime
import db_conn
# import re
from class_scrapers import ClassScraper


class YorkshireClubs(ClassScraper):
    def __init__(self):
        super().__init__()

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
                soup = self.get_html(url)

                p_tags = self.search_tags_alternative('p', soup)

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
                for i in club_list:
                    scraped_clubs.append(i)

            if c["name"] == "Leeds Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

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

            if c["name"] == "York Alpine Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

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

        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output
