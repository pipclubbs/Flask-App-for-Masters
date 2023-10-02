import datetime
from class_scrapers import ClassScraper
import db_conn


class YorkshireClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        p_tag_list = []
        scraped_classes = []
        centres = [
            {
                "area": "yorkshire",
                "name": "The Foundry, Sheffield",
                "classUrl": "https://www.foundryclimbing.com/adult-climbing",
            },
            {
                "area": "yorkshire",
                "name": "Climbing Works, Sheffield",
                "classUrl": "https://www.climbingworks.com/adult-classes",
            },
            {
                "area": "yorkshire",
                "name": "Mad Volume, Hull",
                "classUrl": "https://www.madvolume.co.uk/climbing-classes/",
            },
            {
                "area": "yorkshire",
                "name": "Climbing Lab, Leeds",
                "classUrl": "https://www.climbinglab.co.uk/your-visit-begin/",
            }
        ]

        for c in centres:
            if c["name"] == "The Foundry, Sheffield":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    p_tags = self.search_tags_alternative('p', soup)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[0],
                            "description": p_tags[4],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[0],
                            "description": p_tags[5],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[6],
                            "description": p_tags[8],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[6],
                            "description": p_tags[10],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[6],
                            "description": p_tags[11],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[6],
                            "description": p_tags[12],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[13],
                            "description": p_tags[15],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[13],
                            "description": p_tags[19],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[13],
                            "description": p_tags[20],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[27],
                            "description": p_tags[31],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[27],
                            "description": p_tags[33],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": p_tags[27],
                            "description": p_tags[34],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)
                else:
                    pass

            elif c["name"] == "Climbing Works, Sheffield":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    p_tags = []
                    p_tag_list = self.search_tags('p', soup)
                    for p in p_tag_list:
                        if p != None and p != '\u200b':
                            p_tags.append(p)
                    # print(p_tags)

                    h2_tags = []
                    h2_tag_list = self.search_tags('h2', soup)
                    for i in h2_tag_list:
                        i = i.lower()
                        i = i.title()
                        i = i.replace("'S", "'s")
                        i = i.replace("Abc", "ABC")
                        h2_tags.append(i)

                    span_tags = []
                    span_tags_list = self.search_tags('span', soup)
                    for i in span_tags_list:
                        if i != None and i != "\u200b":
                            span_tags.append(i)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[0],
                            "description": span_tags[8],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[0],
                            "description": p_tags[19],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[1],
                            "description": span_tags[18],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[1],
                            "description": p_tags[23],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[2],
                            "description": span_tags[23],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[2],
                            "description": p_tags[36],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[3],
                            "description": span_tags[28],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[3],
                            "description": p_tags[50],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[4],
                            "description": span_tags[38],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[4],
                            "description": span_tags[39],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[4],
                            "description": span_tags[40],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[5],
                            "description": span_tags[44],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[5],
                            "description": p_tags[57],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[5],
                            "description": p_tags[58],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h2_tags[6],
                            "description": span_tags[48],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

            elif c["name"] == "Mad Volume, Hull":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    span_tags = []
                    span_tag_list = self.search_tags('span', soup)
                    span_tag_list = self.remove_blanks(span_tag_list)
                    for p in span_tag_list:
                        if p != "\xa0":
                            span_tags.append(p)

                    div_tags = []
                    div_tag_list = self.search_tags('div', soup)
                    div_tag_list = self.remove_blanks(div_tag_list)
                    for p in div_tag_list:
                        if p != "\xa0" and p != "\n":
                            div_tags.append(p)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[3],
                            "description": div_tags[0],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[5],
                            "description": div_tags[3],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": span_tags[8],
                            "description": div_tags[5],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

            elif c["name"] == "Climbing Lab, Leeds":
                area = c["area"]
                classUrl = c["classUrl"]
                soup = self.get_html(classUrl)

                if soup:
                    h3_tags = self.search_tags('h3', soup)

                    p_tags = []
                    p_tag_list = self.search_tags_alternative('p', soup)
                    for p in p_tag_list:
                        if p != "\xa0":
                            p_tags.append(p)

                    class_list = [
                        {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h3_tags[1],
                            "description": p_tags[12],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h3_tags[2],
                            "description": p_tags[13],
                            "created": created
                        }, {
                            "area": area,
                            "name": c["name"],
                            "classUrl": classUrl,
                            "title": h3_tags[2],
                            "description": p_tags[16],
                            "created": created
                        }
                    ]
                    for i in class_list:
                        scraped_classes.append(i)

                else:
                    pass

        output.append(db_conn.DatabaseConnection(scraped_classes))
        return output
