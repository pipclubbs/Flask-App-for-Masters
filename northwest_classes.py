import db_conn2
from class_scrapers import ClassScraper


class NorthWestClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
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

                p_tags = self.search_tags_alternative('p', classUrl)
                h6_tags = self.search_tags('h6', classUrl)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[0],
                        "description": p_tags[6]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[1],
                        "description": p_tags[9]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[2],
                        "description": p_tags[12]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[2],
                        "description": p_tags[14]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[2],
                        "description": p_tags[16]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[3],
                        "description": p_tags[18]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[4],
                        "description": p_tags[20]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[5],
                        "description": p_tags[23]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[6],
                        "description": p_tags[26]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h6_tags[6],
                        "description": p_tags[28]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Blochaus Climbing, Manchester":
                area = c["area"]
                classUrl = c["classUrl"]

                span_tags = self.search_tags('span', classUrl)
                span_tags = self.remove_blanks(span_tags)
                span_tags = [i for n, i in enumerate(
                    span_tags) if i not in span_tags[:n]]

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[9],
                        "description": span_tags[10]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[9],
                        "description": span_tags[11]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[16],
                        "description": span_tags[17]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[16],
                        "description": span_tags[18]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[21],
                        "description": span_tags[22]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[21],
                        "description": span_tags[23]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[21],
                        "description": span_tags[24]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[21],
                        "description": span_tags[25]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[28],
                        "description": span_tags[29]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[28],
                        "description": span_tags[30]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": span_tags[28],
                        "description": span_tags[32]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
