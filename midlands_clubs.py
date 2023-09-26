import db_conn
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
                "name": "The Midland Association of Mountaineers",
                "url": "https://www.themam.co.uk/"
            }, {
                "type": "club",
                "area": "midlands",
                "name": "Cave & Crag Club, Birmingham",
                "url": "https://www.caveandcrag.co.uk/"
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

            if c["name"] == "The Midland Association of Mountaineers":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                h1_tags = self.search_tags('h1', soup)
                h2_tags = self.search_tags('h2', soup)
                p_tags = self.search_tags_alternative('p', soup)

                club_list = [
                    {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": p_tags[1],
                        "title": '',
                        "subtitle": h1_tags[1],
                        "description": p_tags[2]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            if c["name"] == "Cave & Crag Club, Birmingham":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                p_tags = self.search_tags('p', soup)
                h2_tags = self.search_tags('h2', soup)
                h3_tags = self.search_tags('h3', soup)

                club_list = [
                    {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": h2_tags[0],
                        "title": '',
                        "subtitle": '',
                        "description": h2_tags[2]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[1]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[2]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h3_tags[0],
                        "description": p_tags[3]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            # print(scraped_clubs)

        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output


# instance = MidlandsClubs()
# instance.assign_values()
