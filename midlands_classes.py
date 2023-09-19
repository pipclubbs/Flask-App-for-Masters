import db_conn2
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

                p_tags = self.search_tags('p', classUrl)
                h2_tags = self.search_tags('h2', classUrl)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[6]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
                        "description": p_tags[7]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
                        "description": p_tags[8]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": p_tags[9]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": p_tags[10]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[4],
                        "description": p_tags[11]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[4],
                        "description": p_tags[12]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[13]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[14]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
