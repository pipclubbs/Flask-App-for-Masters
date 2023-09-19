import db_conn2
from class_scrapers import ClassScraper


class NorthEastClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        p_tag_list = []
        scraped_classes = []
        centres = [
            {
                "area": "north-east",
                "name": "Climb Valley, Newcastle",
                "classUrl": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
            },
            {
                "area": "north-east",
                "name": "Durham Climbing Centre, Durham",
                "classUrl": "https://www.durhamclimbingcentre.co.uk/coaching",
            },
            {
                "area": "north-east",
                "name": "Sunderland Wall, Sunderland",
                "classUrl": "https://sunderlandwall.com/courses/",
            },
            {
                "area": "north-east",
                "name": "Newcastle Climbing Centre, Byker",
                "classUrl": "https://www.newcastleclimbingcentre.co.uk/courses/indoor-courses/",
            }
        ]

        for c in centres:
            if c["name"] == "Climb Valley, Newcastle":
                area = c["area"]
                classUrl = c["classUrl"]
                h1_tag = self.search_tags('h1', classUrl)
                h4_tag = self.search_tags('h4', classUrl)
                p_tag = self.search_tags('p', classUrl)

                for p in p_tag:
                    if p != None and "shopping cart" not in p and "Climb Newcastle Ltd" not in p and "Pick a date" not in p:
                        p_tag_list.append(p)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h1_tag[0],
                        "description": p_tag_list[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h4_tag[0],
                        "description": p_tag_list[1],
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h4_tag[1],
                        "description": p_tag_list[2]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h4_tag[2],
                        "description": p_tag_list[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h4_tag[2],
                        "description": p_tag_list[4]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": c["classUrl"],
                        "title": h4_tag[2],
                        "description": p_tag_list[5]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Durham Climbing Centre, Durham":
                area = c["area"]
                classUrl = c["classUrl"]
                h2_tags = self.search_tags('h2', classUrl)
                h2_tags = self.do_join(h2_tags)

                h3_tags = self.search_tags('h3', classUrl)
                h3_tags = self.remove_blanks(h3_tags)
                h3_tags = self.do_join(h3_tags)

                span_tags = self.search_tags('span', classUrl)
                span_tags = self.remove_blanks(span_tags)

                li_tags = self.search_tags('li', classUrl)
                li_tags = self.remove_blanks(li_tags)

                div_tags = []
                div_tag_list = self.search_tags('div', classUrl)
                for i in div_tag_list:
                    if i != None and "\xa0" not in i and "Contact Us" not in i and "Stay tuned" not in i:
                        div_tags.append(i)
                div_tags = self.do_join(div_tags)

                p_tags = self.search_tags_alternative('p', classUrl)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": div_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": p_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[0],
                        "description": p_tags[1]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[0],
                        "description": p_tags[2]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[0],
                        "description": p_tags[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": div_tags[10]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": div_tags[11]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": p_tags[6]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": p_tags[7]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
                        "description": div_tags[12]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
                        "description": p_tags[8]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Newcastle Climbing Centre, Byker":
                area = c["area"]
                classUrl = c["classUrl"]
                h2_tags = self.search_tags('h2', classUrl)

                span_tags = []
                span_tags_list = self.search_tags('span', classUrl)
                for l in span_tags_list:
                    if l != None and "Facebook" not in l and "Twitter" not in l and "Instagram" not in l and "Book online" not in l and "Select Page" not in l:
                        span_tags.append(l)

                p_tags = []
                p_tag_list = self.search_tags('p', classUrl)
                for j in p_tag_list:
                    if j != None and "Book online" not in j and "Select page" not in j and "Please note that" not in j:
                        p_tags.append(j)

                div_tags = []
                div_tag_list = self.search_tags('div', classUrl)
                for k in div_tag_list:
                    if k != None and "Indoor Courses" not in k and "Our Friends and Sponsors" not in k and "\xa0" not in k:
                        div_tags.append(k)

                strong_tags = self.search_tags('strong', classUrl)
                strong_tags = self.remove_blanks(strong_tags)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[0],
                        "description": p_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[0],
                        "description": p_tags[1]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[2]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[4]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": span_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": span_tags[1]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": span_tags[2]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": span_tags[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": span_tags[4]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
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
                        "title": h2_tags[2],
                        "description": p_tags[9]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[2],
                        "description": p_tags[10]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": div_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": div_tags[1]
                    }, {
                        "area": area, "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": p_tags[11]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": p_tags[12]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[3],
                        "description": p_tags[13]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[4],
                        "description": p_tags[14]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[4],
                        "description": p_tags[15]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[4],
                        "description": strong_tags[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[16]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[17]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[18]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[19]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[20]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[5],
                        "description": p_tags[21]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[6],
                        "description": p_tags[22]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[6],
                        "description": p_tags[23]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h2_tags[6],
                        "description": p_tags[24]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": "",
                        "description": div_tags[3]}
                ]
                for i in class_list:
                    scraped_classes.append(i)

            if c["name"] == "Sunderland Wall, Sunderland":
                area = c["area"]
                classUrl = c["classUrl"]

                h3_tags = self.search_tags('h3', classUrl)
                h4_tags = self.search_tags('h4', classUrl)
                p_tags = self.search_tags('p', classUrl)

                li_tags = []
                li_tag_list = self.search_tags_alternative('li', classUrl)
                li_tag_list = self.remove_blanks(li_tag_list)
                for t in li_tag_list:
                    if len(t) > 25:
                        li_tags.append(t)

                class_list = [
                    {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": p_tags[1]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": li_tags[6]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": li_tags[7]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": li_tags[8]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": li_tags[9]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[0],
                        "description": li_tags[10]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": p_tags[2]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": li_tags[11]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": li_tags[12]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": li_tags[13]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": h4_tags[0]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": p_tags[3]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": h4_tags[1]
                    }, {
                        "area": area,
                        "name": c["name"],
                        "classUrl": classUrl,
                        "title": h3_tags[1],
                        "description": p_tags[4]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
