import db_conn2
from class_scrapers import ClassScraper


class NorthWestClubs(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
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
            '''if c["name"] == "West Cumbria Mountaineering Club":
                area = c["area"]
                url = c["url"]
                soup = self.get_html(url)

                span_tags = self.search_tags('span', soup)
                p_tags = self.search_tags_alternative('p', soup)

                club_list = [
                    {
                        "type": "club",
                        "area": area,
                        "name": c["name"],
                        "url": url,
                        "intro": f'{span_tags[0]}{span_tags[1]}',
                        "title": '',
                        "subtitle": '',
                        "description": p_tags[0]
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
                        "subtitle": '',
                        "description": p_tags[3]
                    }
                ]
                for i in club_list:
                    scraped_clubs.append(i)

            if c["name"] == "Kendal Mountaineering Club":
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

            if c["name"] == "The Wayfarer's Club":
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
                    scraped_clubs.append(i)

            # print(scraped_clubs)

        output.append(db_conn2.DatabaseConnection(scraped_clubs))
        return output


# instance = NorthWestClubs()
# instance.assign_values()
