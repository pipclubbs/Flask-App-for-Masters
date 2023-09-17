# from bs4 import BeautifulSoup
# import requests
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
                "name": "Climb Valley, Newcastle",
                "url": "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials",
            },
            {
                "name": "Durham Climbing Centre, Durham",
                "url": "https://www.durhamclimbingcentre.co.uk/coaching",
            },
            {
                "name": "Sunderland Wall, Sunderland",
                "url": "https://sunderlandwall.com/courses/",
            },
            {
                "name": "Newcastle Climbing Centre, Byker",
                "url": "https://www.newcastleclimbingcentre.co.uk/courses/indoor-courses/",
            }
        ]

        for c in centres:
            if c["name"] == "Climb Valley, Newcastle":
                url = c["url"]
                h1_tag = self.search_tags('h1', url)
                h4_tag = self.search_tags('h4', url)
                p_tag = self.search_tags('p', url)

                for p in p_tag:
                    if p != None and "shopping cart" not in p and "Climb Newcastle Ltd" not in p and "Pick a date" not in p:
                        p_tag_list.append(p)

                class_list = [
                    {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h1_tag[0],
                        "description": p_tag_list[0]
                    }, {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h4_tag[0],
                        "description": p_tag_list[1],
                    }, {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h4_tag[1],
                        "description": p_tag_list[2]
                    }, {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h4_tag[2],
                        "description": p_tag_list[3]
                    }, {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h4_tag[2],
                        "description": p_tag_list[4]
                    }, {
                        "name": c["name"],
                        "url": c["url"],
                        "title": h4_tag[2],
                        "description": p_tag_list[5]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Durham Climbing Centre, Durham":
                url = c["url"]
                h2_tags = self.search_tags('h2', url)
                h2_tags = self.do_join(h2_tags)

                h3_tags = self.search_tags('h3', url)
                h3_tags = self.remove_blanks(h3_tags)
                h3_tags = self.do_join(h3_tags)

                span_tags = self.search_tags('span', url)
                span_tags = self.remove_blanks(span_tags)

                li_tags = self.search_tags('li', url)
                li_tags = self.remove_blanks(li_tags)

                div_tags = []
                div_tag_list = self.search_tags('div', url)
                for i in div_tag_list:
                    if i != None and "\xa0" not in i and "Contact Us" not in i and "Stay tuned" not in i:
                        div_tags.append(i)
                div_tags = self.do_join(div_tags)

                p_tags = self.search_tags_alternative('p', url)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": div_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": p_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[2]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[3]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": div_tags[10]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": div_tags[11]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": p_tags[6]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": p_tags[7]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": div_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": p_tags[8]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

            elif c["name"] == "Newcastle Climbing Centre, Byker":
                url = c["url"]
                h2_tags = self.search_tags('h2', url)

                span_tags = []
                span_tags_list = self.search_tags('span', url)
                for l in span_tags_list:
                    if l != None and "Facebook" not in l and "Twitter" not in l and "Instagram" not in l and "Book online" not in l and "Select Page" not in l:
                        span_tags.append(l)

                p_tags = []
                p_tag_list = self.search_tags('p', url)
                for j in p_tag_list:
                    if j != None and "Book online" not in j and "Select page" not in j and "Please note that" not in j:
                        p_tags.append(j)

                div_tags = []
                div_tag_list = self.search_tags('div', url)
                for k in div_tag_list:
                    if k != None and "Indoor Courses" not in k and "Our Friends and Sponsors" not in k and "\xa0" not in k:
                        div_tags.append(k)

                strong_tags = self.search_tags('strong', url)
                strong_tags = self.remove_blanks(strong_tags)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[0],
                        "description": p_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[2]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[3]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[4]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[2]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[3]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": span_tags[4]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[1],
                        "description": p_tags[5]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
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
                        "title": h2_tags[2],
                        "description": p_tags[9]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[2],
                        "description": p_tags[10]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": div_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": div_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[11]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[3],
                        "description": p_tags[13]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": p_tags[14]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": p_tags[15]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[4],
                        "description": strong_tags[3]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[16]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[17]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[18]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[19]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[20]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[5],
                        "description": p_tags[21]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[6],
                        "description": p_tags[22]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[6],
                        "description": p_tags[23]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h2_tags[6],
                        "description": p_tags[24]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": "",
                        "description": div_tags[3]}
                ]
                for i in class_list:
                    scraped_classes.append(i)

            if c["name"] == "Sunderland Wall, Sunderland":
                url = c["url"]

                h3_tags = self.search_tags('h3', url)
                h4_tags = self.search_tags('h4', url)
                p_tags = self.search_tags('p', url)

                li_tags = []
                li_tag_list = self.search_tags_alternative('li', url)
                li_tag_list = self.remove_blanks(li_tag_list)
                for t in li_tag_list:
                    if len(t) > 25:
                        li_tags.append(t)

                class_list = [
                    {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": p_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": li_tags[6]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": li_tags[7]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": li_tags[8]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": li_tags[9]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[0],
                        "description": li_tags[10]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": p_tags[2]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": li_tags[11]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": li_tags[12]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": li_tags[13]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": h4_tags[0]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": p_tags[3]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": h4_tags[1]
                    }, {
                        "name": c["name"],
                        "url": url,
                        "title": h3_tags[1],
                        "description": p_tags[4]
                    }
                ]
                for i in class_list:
                    scraped_classes.append(i)

        output.append(db_conn2.DatabaseConnection(scraped_classes))
        return output

    '''def __init__(self):
        self.name = ""
        self.url = ""
        self.title = ""
        self.description = ""

    def get_html(self, url):
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        return soup

    def search_tags(self, tag, url):
        url = url
        soup = self.get_html(url)
        searched_soup = soup.find_all(tag)
        tag_list = [e.string for e in searched_soup]
        return tag_list

    def search_tags_alternative(self, tag, url):
        url = url
        soup = self.get_html(url)
        tag_list = []
        tags = soup.find_all(tag)
        for e in tags:
            e = e.text
            tag_list.append(e)
        return tag_list

    def remove_blanks(self, list):
        new_list = []
        for i in list:
            if i != None:
                new_list.append(i)
        return new_list

    def do_join(self, list):
        list = list
        new_list = []
        for j in list:
            j = " ".join(j.split())
            new_list.append(j)
        return new_list'''
