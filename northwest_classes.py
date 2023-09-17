import db_conn2
from class_scrapers import ClassScraper


class NorthWestClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        p_tag_list = []
        scraped_classes = []
        centres = [
            {
                "name": "Eden Rock, Carlisle",
                "url": "https://www.edenrockclimbing.com/adult-classes-carlisle",
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
            if c["name"] == "Eden Rock, Carlisle":
                url = c["url"]

                p_tags = self.search_tags_alternative('p', url)
                h6_tags = self.search_tags('h6', url)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[0],
                        "description": p_tags[6]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[1],
                        "description": p_tags[9]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[2],
                        "description": p_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[2],
                        "description": p_tags[14]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[2],
                        "description": p_tags[16]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[3],
                        "description": p_tags[18]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[4],
                        "description": p_tags[20]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[5],
                        "description": p_tags[23]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[6],
                        "description": p_tags[26]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h6_tags[6],
                        "description": p_tags[28]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
