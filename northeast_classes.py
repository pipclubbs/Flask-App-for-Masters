"""module containing the class that scrapes websites for climbing class data (North East)"""
import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthEastClasses(ClassScraper):
    """class containing the web scraping information for climbing classes (North East)"""
    def __init__(self):
        super().__init__()


    """method that defines the sites to scrape, then runs through each in turn and sorts the
    results into dictionaries ready for storing in the database"""
    def assign_values(self):
        created = datetime.datetime.now()
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
            try:
                if c["name"] == "Climb Valley, Newcastle":
                    area = c["area"]
                    classUrl = c["classUrl"]
                    soup = self.get_html(classUrl) # get the html via the parent class method
    
                    if soup:
                        # search for the tags in the html
                        h1_tag = self.search_tags('h1', soup)
                        h4_tag = self.search_tags('h4', soup)
                        p_tag = self.search_tags('p', soup)
    
                        # extra tidies for the p_tag
                        for p in p_tag:
                            if p != None and "shopping cart" not in p and "Climb Newcastle Ltd" not in p and "Pick a date" not in p:
                                p_tag_list.append(p)
    
                        # allocate the results to a dictionary for storing in the database
                        class_list = [
                            {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h1_tag[0],
                                "description": p_tag_list[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h4_tag[0],
                                "description": p_tag_list[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h4_tag[1],
                                "description": p_tag_list[2],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h4_tag[2],
                                "description": p_tag_list[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h4_tag[2],
                                "description": p_tag_list[4],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": c["classUrl"],
                                "title": h4_tag[2],
                                "description": p_tag_list[5],
                                "created": created
                            }
                        ]
                        # add each dictionary entry to a list
                        for i in class_list:
                            scraped_classes.append(i)
                    else:
                        pass

            except:
                pass

            try:
                if c["name"] == "Durham Climbing Centre, Durham":
                    area = c["area"]
                    classUrl = c["classUrl"]
                    soup = self.get_html(classUrl)
    
                    if soup:
                        h2_tags = self.search_tags('h2', soup)
                        h2_tags = self.do_join(h2_tags)
    
                        h3_tags = self.search_tags('h3', soup)
                        h3_tags = self.remove_blanks(h3_tags)
                        h3_tags = self.do_join(h3_tags)
    
                        span_tags = self.search_tags('span', soup)
                        span_tags = self.remove_blanks(span_tags)
    
                        li_tags = self.search_tags('li', soup)
                        li_tags = self.remove_blanks(li_tags)
    
                        div_tags = []
                        div_tag_list = self.search_tags('div', soup)
                        for i in div_tag_list:
                            if i != None and "\xa0" not in i and "Contact Us" not in i and "Stay tuned" not in i:
                                div_tags.append(i)
                        div_tags = self.do_join(div_tags)
    
                        p_tags = self.search_tags_alternative('p', soup)
    
                        class_list = [
                            {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": div_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": p_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[0],
                                "description": p_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[0],
                                "description": p_tags[2],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[0],
                                "description": p_tags[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": div_tags[10],
                                "created": created
                            }, {
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
                                "title": h3_tags[1],
                                "description": div_tags[11],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": p_tags[6],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": p_tags[7],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[2],
                                "description": div_tags[12],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[2],
                                "description": p_tags[8],
                                "created": created
                            }
                        ]
                        for i in class_list:
                            scraped_classes.append(i)
    
                    else:
                        pass

            except:
                pass

            try:
                if c["name"] == "Newcastle Climbing Centre, Byker":
                    area = c["area"]
                    classUrl = c["classUrl"]
                    soup = self.get_html(classUrl)
    
                    if soup:
                        h2_tags = self.search_tags('h2', soup)
    
                        span_tags = []
                        span_tags_list = self.search_tags('span', soup)
                        for l in span_tags_list:
                            if l != None and "Facebook" not in l and "Twitter" not in l and "Instagram" not in l and "Book online" not in l and "Select Page" not in l:
                                span_tags.append(l)
    
                        p_tags = []
                        p_tag_list = self.search_tags('p', soup)
                        for j in p_tag_list:
                            if j != None and "Book online" not in j and "Select page" not in j and "Please note that" not in j:
                                p_tags.append(j)
    
                        div_tags = []
                        div_tag_list = self.search_tags('div', soup)
                        for k in div_tag_list:
                            if k != None and "Indoor Courses" not in k and "Our Friends and Sponsors" not in k and "\xa0" not in k:
                                div_tags.append(k)
    
                        strong_tags = self.search_tags('strong', soup)
                        strong_tags = self.remove_blanks(strong_tags)
    
                        class_list = [
                            {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[0],
                                "description": p_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[0],
                                "description": p_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": p_tags[2],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": p_tags[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": p_tags[4],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": span_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": span_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": span_tags[2],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": span_tags[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[1],
                                "description": span_tags[4],
                                "created": created
                            }, {
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
                                "title": h2_tags[2],
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
                                "title": h2_tags[2],
                                "description": p_tags[9],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[2],
                                "description": p_tags[10],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[3],
                                "description": div_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[3],
                                "description": div_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[3],
                                "description": p_tags[11],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[3],
                                "description": p_tags[12],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[3],
                                "description": p_tags[13],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[4],
                                "description": p_tags[14],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[4],
                                "description": p_tags[15],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[4],
                                "description": strong_tags[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[16],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[17],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[18],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[19],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[20],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[5],
                                "description": p_tags[21],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[6],
                                "description": p_tags[22],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[6],
                                "description": p_tags[23],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h2_tags[6],
                                "description": p_tags[24],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": "",
                                "description": div_tags[3],
                                "created": created
                            }
                        ]
                        for i in class_list:
                            scraped_classes.append(i)
                    else:
                        pass

            except:
                pass
                
            try:
                if c["name"] == "Sunderland Wall, Sunderland":
                    area = c["area"]
                    classUrl = c["classUrl"]
                    soup = self.get_html(classUrl)
    
                    if soup:
                        h3_tags = self.search_tags('h3', soup)
                        h4_tags = self.search_tags('h4', soup)
                        p_tags = self.search_tags('p', soup)
    
                        li_tags = []
                        li_tag_list = self.search_tags_alternative('li', soup)
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
                                "description": p_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": li_tags[6],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": li_tags[7],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": li_tags[8],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": li_tags[9],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[0],
                                "description": li_tags[10],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": p_tags[2],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": li_tags[11],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": li_tags[12],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": li_tags[13],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": h4_tags[0],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": p_tags[3],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": h4_tags[1],
                                "created": created
                            }, {
                                "area": area,
                                "name": c["name"],
                                "classUrl": classUrl,
                                "title": h3_tags[1],
                                "description": p_tags[4],
                                "created": created
                            }
                        ]
                        for i in class_list:
                            scraped_classes.append(i)
    
                    else:
                        pass

            except:
                pass

        """send the compiled scraped class list to the database module, 
        and append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_classes))
        return output
