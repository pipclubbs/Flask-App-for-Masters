import db_conn
import datetime
from class_scrapers import ClassScraper


class MidlandsClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        scraped_classes = []
        centres = [
            {
                "area": "midlands",
                "name": "YMCA Lincolnshire, Lincoln",
                "classUrl": "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/lessons-sessions/",
            },
        ]

        for c in centres:

            if c["name"] == "YMCA Lincolnshire, Lincoln":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)
                created = datetime.datetime.now()

                if soup:
                    p_tags = self.search_tags('p', soup)
                    h2_tags = self.search_tags('h2', soup)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[1],
                            "description": p_tags[5],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[1],
                            "description": p_tags[6],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[2],
                            "description": p_tags[7],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[2],
                            "description": p_tags[8],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[3],
                            "description": p_tags[9],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[3],
                            "description": p_tags[10],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[4],
                            "description": p_tags[11],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[4],
                            "description": p_tags[12],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[5],
                            "description": p_tags[13],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[5],
                            "description": p_tags[14],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

        output.append(db_conn.DatabaseConnection(scraped_classes))
        return output
