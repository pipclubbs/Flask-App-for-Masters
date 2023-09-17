import db_conn2
from class_scrapers import ClassScraper


class MidlandsClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        p_tag_list = []
        scraped_classes = []
        centres = [
            {
                "name": "YMCA Lincolnshire, Lincoln",
                "url": "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/lessons-sessions/",
            },
            {
                "name": "",
                "url": "",
            },
            {
                "name": "",
                "url": "",
            },
            {
                "name": "",
                "url": "",
            }
        ]

        for c in centres:
            if c["name"] == "YMCA Lincolnshire, Lincoln":
                url = c["url"]

                p_tags = self.search_tags('p', url)
                h2_tags = self.search_tags('h2', url)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[6]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": p_tags[7]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": p_tags[8]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[9]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[10]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": p_tags[11]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": p_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[13]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[14]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
