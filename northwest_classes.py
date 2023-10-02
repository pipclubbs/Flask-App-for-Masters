import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthWestClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        scraped_classes = []
        centres = [
            {
                "area": "north-west",
                "name": "Eden Rock, Carlisle",
                "classUrl": "https://www.edenrockclimbing.com/adult-classes-carlisle",
            },
            {
                "area": "north-west",
                "name": "Blochaus Climbing, Manchester",
                "classUrl": "https://www.blochausclimbing.com/courses",
            }
        ]

        for c in centres:
            if c["name"] == "Eden Rock, Carlisle":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    p_tags = self.search_tags_alternative('p', soup)
                    h6_tags = self.search_tags('h6', soup)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[0],
                            "description": p_tags[6],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[1],
                            "description": p_tags[9],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[2],
                            "description": p_tags[12],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[2],
                            "description": p_tags[14],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[2],
                            "description": p_tags[16],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[3],
                            "description": p_tags[18],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[4],
                            "description": p_tags[20],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[5],
                            "description": p_tags[23],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[6],
                            "description": p_tags[26],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h6_tags[6],
                            "description": p_tags[28],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

            elif c["name"] == "Blochaus Climbing, Manchester":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    span_tags = self.search_tags('span', soup)
                    span_tags = self.remove_blanks(span_tags)
                    span_tags = [i for n, i in enumerate(
                        span_tags) if i not in span_tags[:n]]

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[9],
                            "description": span_tags[10],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[9],
                            "description": span_tags[11],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[16],
                            "description": span_tags[17],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[16],
                            "description": span_tags[18],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[21],
                            "description": span_tags[22],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[21],
                            "description": span_tags[23],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[21],
                            "description": span_tags[24],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[21],
                            "description": span_tags[25],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[28],
                            "description": span_tags[29],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[28],
                            "description": span_tags[30],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[28],
                            "description": span_tags[32],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

        output.append(db_conn.DatabaseConnection(scraped_classes))
        return output
