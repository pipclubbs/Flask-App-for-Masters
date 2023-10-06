"""module containing the class that scrapes websites for climbing venue data (North West)"""
import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthWestContacts(ClassScraper):
    """class containing the web scraping information for climbing clubs (North West)"""
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
                "area": "north-west",
                "name": "Eden Rock, Carlisle",
                "contactUrl": "https://www.edenrockclimbing.com/contact-carlisle",
                "homeUrl": "https://www.edenrockclimbing.com/carlisle-home"
            },
            {
                "area": "north-west",
                "name": "Blochaus Climbing, Manchester",
                "contactUrl": "https://www.blochausclimbing.com/contact-us",
                "homeUrl": "https://www.blochausclimbing.com/"
            }
        ]

        for c in centres:
            if c["name"] == "Eden Rock, Carlisle":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl) # get the html via the parent class

                if soup:
                    # search for the tags in the html
                    span_tags = self.search_tags('span', soup)
                    span_tags = [i for n, i in enumerate(
                        span_tags) if i not in span_tags[:n]]

                    # allocate the results to a dictionary for storing in the database
                    centre_details = [
                        {
                            "area": area,
                            "name": c["name"],
                            "homeUrl": c["homeUrl"],
                            "contactUrl": contactUrl,
                            "classUrl": '',
                            "street": span_tags[4],
                            "street_area": span_tags[5],
                            "city": span_tags[6],
                            "postcode": span_tags[7],
                            "email": span_tags[10],
                            "phone": span_tags[12],
                            "created": created
                        }
                    ]
                    # append the dictionary to a list
                    for i in centre_details:
                        scraped_centres.append(i)

                else:
                    pass

            if c["name"] == "Blochaus Climbing, Manchester":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                if soup:
                    p_tags = self.search_tags('p', soup)

                    centre_details = [
                        {
                            "area": area,
                            "name": c["name"],
                            "homeUrl": c["homeUrl"],
                            "contactUrl": contactUrl,
                            "classUrl": '',
                            "street": p_tags[13],
                            "street_area": p_tags[14],
                            "city": p_tags[15],
                            "postcode": p_tags[16],
                            "email": p_tags[24],
                            "phone": p_tags[23],
                            "created": created
                        }
                    ]
                    for i in centre_details:
                        scraped_centres.append(i)

                else:
                    pass

        """send the compiled centre list to the database module, and
        append the result to the output list"""
        output.append(db_conn.DatabaseConnection(scraped_centres))
        return output
