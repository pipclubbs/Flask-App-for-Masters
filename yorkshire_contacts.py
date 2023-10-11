"""module containing the class that scrapes websites for climbing centre data (Yorkshire)"""
import datetime
import re
import db_conn
from class_scrapers import ClassScraper


class YorkshireContacts(ClassScraper):
    """class containing the web scraping information for climbing centres (Yorkshire)"""
    def __init__(self):
        super().__init__()


    """method that defines the sites to scrape, then runs through each in turn and sorts the results
    into dictionaries ready for storing in the database"""
    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        scraped_centres = []
        centres = [
            {
                "area": "yorkshire",
                "name": "The Foundry, Sheffield",
                "contactUrl": "https://www.foundryclimbing.com/",
                "homeUrl": "https://www.foundryclimbing.com/"
            }, {
                "area": "yorkshire",
                "name": "Climbing Works, Sheffield",
                "contactUrl": "https://www.climbingworks.com/find-us",
                "homeUrl": "https://www.climbingworks.com/"
            }, {
                "area": "yorkshire",
                "name": "Mad Volume, Hull",
                "contactUrl": "https://www.madvolume.co.uk/",
                "homeUrl": "https://www.madvolume.co.uk/"
            }, {
                "area": "yorkshire",
                "name": "Climbing Lab, Leeds",
                "contactUrl": "https://www.climbinglab.co.uk/your-visit-begin/",
                "homeUrl": "https://www.climbinglab.co.uk/"
            }
        ]

        for c in centres:
            try:
                if c["name"] == "The Foundry, Sheffield":
                    contactUrl = c["contactUrl"]
                    area = c["area"]
                    soup = self.get_html(contactUrl) # get html via the parent class
    
                    if soup:
                        # search for the tags in the html
                        div_tags = self.search_tags('div', soup)
                        div_tags = self.remove_blanks(div_tags)
                        div_tags = self.tidy_tags(div_tags)
    
                        div_tags_street = re.sub(r'([a-z])(,)', r'\1', div_tags[6])
                        div_tags_address = re.sub(
                            r'([A-z])(,)', r'\1', div_tags[7])
                        div_tags_address = div_tags_address.split()
    
                        a_tags = self.search_tags('a', soup)
                        a_tags = self.remove_blanks(a_tags)
                        a_tags = self.tidy_tags(a_tags)
    
                        # allocate the results to a dictionary for storing in the database
                        centre_details = [
                            {
                                "area": area,
                                "name": c["name"],
                                "homeUrl": c["homeUrl"],
                                "contactUrl": contactUrl,
                                "classUrl": '',
                                "street": div_tags_street,
                                "street_area": '',
                                "city": div_tags_address[0],
                                "postcode": f'{div_tags_address[2]} {div_tags_address[3]}',
                                "email": a_tags[33],
                                "phone": a_tags[32],
                                "created": created
                            }
                        ]
                        
                        for i in centre_details:
                            scraped_centres.append(i)
    
                    else:
                        pass

            except:
                pass

            try:
                if c["name"] == "Climbing Works, Sheffield":
                    contactUrl = c["contactUrl"]
                    area = c["area"]
                    soup = self.get_html(contactUrl)
    
                    if soup:
                        span_tags = self.search_tags_alternative('span', soup)
                        span_tags_address = re.sub(r'(\n)', r' ', span_tags[41])
                        span_tags_address = re.sub(
                            r'([a-z])(,)', r'\1', span_tags_address)
                        span_tags_address = span_tags_address.split()
    
                        centre_details = [
                            {
                                "area": area,
                                "name": c["name"],
                                "homeUrl": c["homeUrl"],
                                "contactUrl": contactUrl,
                                "classUrl": '',
                                "street": f'{span_tags_address[3]} {span_tags_address[4]} {span_tags_address[5]} {span_tags_address[6]}',
                                "street_area": f'{span_tags_address[7]} {span_tags_address[8]} {span_tags_address[9]} {span_tags_address[10]}',
                                "city": span_tags_address[11],
                                "postcode": span_tags[43],
                                "email": span_tags[39],
                                "phone": span_tags[40],
                                "created": created
                            }
                        ]
                        for i in centre_details:
                            scraped_centres.append(i)
    
                    else:
                        pass

            except:
                pass

            try:
                if c["name"] == "Mad Volume, Hull":
                    contactUrl = c["contactUrl"]
                    area = c["area"]
                    soup = self.get_html(contactUrl)
    
                    if soup:
                        span_tags = self.search_tags('span', soup)
                        span_tags = self.remove_blanks(span_tags)
                        span_tags = self.tidy_tags(span_tags)
    
                        div_tags = self.search_tags('div', soup)
                        div_tags = self.remove_blanks(div_tags)
                        div_tags = self.tidy_tags(div_tags)
                        div_tags_address = re.sub(r'( \| )', r' ', div_tags[86])
                        div_tags_address = div_tags_address.split()
    
                        centre_details = [
                            {
                                "area": area,
                                "name": c["name"],
                                "homeUrl": c["homeUrl"],
                                "contactUrl": contactUrl,
                                "classUrl": '',
                                "street": f'{div_tags_address[0]} {div_tags_address[1]}',
                                "street_area": f'{div_tags_address[2]} {div_tags_address[3]}',
                                "city": "Hull",
                                "postcode": div_tags[87],
                                "email": span_tags[0],
                                "phone": f'{span_tags[94]}',
                                "created": created
                            }
                        ]
                        for i in centre_details:
                            scraped_centres.append(i)
    
                    else:
                        pass

            except:
                pass

            try:
                if c["name"] == "Climbing Lab, Leeds":
                    contactUrl = c["contactUrl"]
                    area = c["area"]
                    soup = self.get_html(contactUrl)
    
                    if soup:
                        p_tags = self.search_tags('p', soup)
                        p_tags = self.remove_blanks(p_tags)
                        p_tags = self.tidy_tags(p_tags)
    
                        centre_details = [
                            {
                                "area": area,
                                "name": c["name"],
                                "homeUrl": c["homeUrl"],
                                "contactUrl": contactUrl,
                                "classUrl": '',
                                "street": p_tags[9],
                                "street_area": p_tags[10],
                                "city": p_tags[11],
                                "postcode": p_tags[12],
                                "email": p_tags[13],
                                "phone": '',
                                "created": created
                            }
                        ]
                        for i in centre_details:
                            scraped_centres.append(i)
    
                    else:
                        pass

            except:
                pass

        """send the compiled centre list to the database module, and 
        append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_centres))
        return output


    """method to tidy the tags"""
    def tidy_tags(self, list):
        new_list = []
        for i in list:
            if i != '\xa0' and i != '\n':
                new_list.append(i)
        return new_list
