from bs4 import BeautifulSoup
import requests
from class_scrapers import ClassScraper
import db_conn2
import json


class YorkshireClasses(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
        p_tag_list = []
        scraped_classes = []
        centres = [
            {
                "name": "The Foundry, Sheffield",
                "url": "https://www.foundryclimbing.com/adult-climbing",
            },
            {
                "name": "Climbing Works, Sheffield",
                "url": "https://www.climbingworks.com/adult-classes",
            },
            {
                "name": "Mad Valume, Hull",
                "url": "",
            },
            {
                "name": "Climbing Lab, Leeds",
                "url": "",
            }
        ]

        for c in centres:
            if c["name"] == "The Foundry, Sheffield":
                url = c["url"]
                p_tags = self.search_tags_alternative('p', url)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[0],
                        "description": p_tags[4]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[0],
                        "description": p_tags[5]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[6],
                        "description": p_tags[8]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[6],
                        "description": p_tags[10]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[6],
                        "description": p_tags[11]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[6],
                        "description": p_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[13],
                        "description": p_tags[15]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[13],
                        "description": p_tags[19]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[13],
                        "description": p_tags[20]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[27],
                        "description": p_tags[31]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[27],
                        "description": p_tags[33]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": p_tags[27],
                        "description": p_tags[34]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Climbing Works, Sheffield":
                url = c["url"]

                p_tags = []
                p_tag_list = self.search_tags('p', url)
                for p in p_tag_list:
                    if p != None and p != '\u200b':
                        p_tags.append(p)
                print(p_tags)

                h2_tags = []
                h2_tag_list = self.search_tags('h2', url)
                for i in h2_tag_list:
                    i = i.lower()
                    i = i.title()
                    i = i.replace("'S", "'s")
                    i = i.replace("Abc", "ABC")
                    h2_tags.append(i)

                span_tags = []
                span_tags_list = self.search_tags('span', url)
                for i in span_tags_list:
                    if i != None and i != "\u200b":
                        span_tags.append(i)
                # with open("saved_classes.json", "a") as file:
                #    json.dump(span_tags, file, indent=4)
                '''print(type(span_tag_list))
                for i in span_tag_list:
                    if "If you are a novice" in i or "The ABCs of climbing" in i or "A free coaching session" in i or "Three sessions to get" in i or "Take your climbing outdoors" in i or "coaching sessions with our experienced" in i:
                        span_tags.append(i)
                print(span_tags)'''

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": span_tags[8]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[19]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[18]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[23]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": span_tags[23]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": p_tags[36]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": span_tags[28]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[50]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": span_tags[38]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": span_tags[39]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": span_tags[40]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": span_tags[44]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[57]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[58]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[6],
                        "description": span_tags[48]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)
                # print(scraped_classes)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output
