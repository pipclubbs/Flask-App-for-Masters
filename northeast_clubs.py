import db_conn
from class_scrapers import ClassScraper


class NorthEastClubs(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
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
                soup = self.get_html(url)

                h4_tags = self.search_tags('h4', soup)
                p_tags = self.search_tags('p', soup)

                club_list = [
                    {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": h4_tags[1],  # the club caters for
                        "title": h4_tags[2],  # a little bit...
                        "subtitle": h4_tags[3],  # social
                        "description": p_tags[2]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": h4_tags[1],  # the club caters for
                        "title": h4_tags[2],  # a little bit...
                        "subtitle": h4_tags[4],  # experienced
                        "description": p_tags[3]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": h4_tags[1],  # the club caters for
                        "title": h4_tags[2],  # a little bit...
                        "subtitle": h4_tags[5],  # active
                        "description": p_tags[4]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            if c["name"] == "Sunderland Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

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
                        "description": span_tags[4]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": span_tags[2],  # climbing
                        "subtitle": '',
                        "description": span_tags[5]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": span_tags[2],  # climbing
                        "subtitle": '',
                        "description": span_tags[6]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            if c["name"] == "Durham Mountain Sports":
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
                        "intro": p_tags[0],
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
                        "subtitle": '',
                        "description": p_tags[3]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[4]
                    }, {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[5]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

                print(scraped_clubs)

        output.append(db_conn.DatabaseConnection(scraped_clubs))
        return output
# instance = NorthEastClubs()
# instance.assign_values()
