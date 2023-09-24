import db_conn2
from class_scrapers import ClassScraper


class MidlandsClubs(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        scraped_clubs = []
        clubs = [
            {
                "type": "club",
                "area": "midlands",
                "name": "Solihull Mountaineering Club",
                "url": "http://www.solihullmc.org.uk/"
            }, {
                "type": "club",
                "area": "midlands",
                "name": "",
                "url": ""
            }, {
                "type": "club",
                "area": "midlands",
                "name": "",
                "url": ""
            }
        ]

        for c in clubs:
            if c["name"] == "Solihull Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                p_tags = self.search_tags_alternative('p', soup)
                p_tag_list = []
                p_tags_updated = []
                for tag in p_tags:
                    p_tag_list.append(tag.replace("\n\n", ""))
                for tag in p_tag_list:
                    p_tags_updated.append(tag.replace("\n", ""))

                club_list = [
                    {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags_updated[4]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags_updated[5]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags_updated[6]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags_updated[7]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags_updated[8]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            '''if c["name"] == "Kendal Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

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
                        "description": p_tags[1]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[0],
                        "subtitle": '',
                        "description": p_tags[2]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[1],
                        "subtitle": '',
                        "description": p_tags[5]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[1],
                        "subtitle": '',
                        "description": p_tags[6]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[1],
                        "subtitle": '',
                        "description": p_tags[7]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[1],
                        "subtitle": '',
                        "description": p_tags[8]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[2],
                        "subtitle": '',
                        "description": p_tags[9]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[2],
                        "subtitle": '',
                        "description": p_tags[10]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": h2_tags[2],
                        "subtitle": '',
                        "description": p_tags[11]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)'''

            '''if c["name"] == "The Wayfarer's Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

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
                        "description": p_tags[8]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[9]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[10]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[11]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)'''

            # print(scraped_clubs)

        output.append(db_conn2.DatabaseConnection(scraped_clubs))
        return output


# instance = MidlandsClubs()
# instance.assign_values()
