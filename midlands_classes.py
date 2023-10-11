"""module containing the class that scrapes websites for climbing class data (Midlands)""" 
import db_conn
import datetime
from class_scrapers import ClassScraper


class MidlandsClasses(ClassScraper):
    """class containing the web scraping information for climbing classes (Midlands)"""
    def __init__(self):
        super().__init__()


    """method that defines the sites to scrape, then runs through each in turn and sorts
    the results into dictionaries ready for storing in the database"""
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
            try:
                if c["name"] == "YMCA Lincolnshire, Lincoln":
                    area = c["area"]
                    classUrl = c["classUrl"]
                    soup = self.get_html(classUrl) # get the html via the parent class method
                    created = datetime.datetime.now()
    
                    if soup:
                        # search for the tags in the html
                        p_tags = self.search_tags('p', soup)
                        h2_tags = self.search_tags('h2', soup)
    
                        # allocate the results to a dictionary for storing in the database
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
                        # add each dictionary entry to a list
                        for i in class_list:
                            scraped_classes.append(i)
    
                    else:
                        pass

            except:
                pass

        """send the compiled scraped events list to the database module, 
        and append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_classes))
        return output
