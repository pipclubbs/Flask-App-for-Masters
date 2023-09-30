"""module containing the class that scrapes websites for climbing 
event data"""

import datetime
# import db_conn
from class_scrapers import ClassScraper
from async_scrape import AsyncScraper


class Events(ClassScraper, AsyncScraper):
    """class containing the web scraping information for events websites"""

    def __init__(self):
        super().__init__()

    def assign_values(self):
        """method that defines the sites to scrape, then runs through each in 
        turn, and sorts the results into dictionaries ready for storing in the database"""
        created = datetime.datetime.now()
        # output = []
        scraped_events = []
        events = [
            {
                "name": "Brit Rock Film Tour",
                "url": "https://www.britrockfilmtour.com/",
                "event": "event"
            }, {
                "name": "Women's Climbing Symposium",
                "url": "https://www.womensclimbingsymposium.com/wcs23",
                "event": "event"
            }, {
                "name": "Speakers from the Edge",
                "url": "https://www.speakersfromtheedge.com/theatre-tours",
                "event": "event"
            }
        ]

        # send urls to the asynchronous scraper as a list
        event_urls = []
        for dictionary in events:
            event_urls.append(dictionary["url"])

        soups = []
        returned_soup = AsyncScraper()
        returned_soup.start_scrape(event_urls)

        # add each of the returned soups to a list
        for item in returned_soup.soups:
            soups.append(item)

        for soup in soups:
            # extract the title tags from each soup for identification
            titles = []
            title = self.search_tags('title', soup)
            titles.append(title)

            # once identified, pull out the tags from the html and sort
            for item in titles:

                if item[0] == 'Brit Rock Film Tour | 2023':
                    url = "https://www.britrockfilmtour.com/"
                    name = "Brit Rock Film Tour"

                    # search for the tags in the html soup
                    h1_tags = self.search_tags_alternative('h1', soup)
                    p_tags = self.search_tags_alternative('p', soup)
                    p_tags = self.strip_spaces_and_breaks(p_tags)

                    # allocate the results to a dictionary for storing in the database
                    event_list = [
                        {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": p_tags[1],
                            "title": '',
                            "subtitle": '',
                            "description": "View web site for full event listings",
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": h1_tags[2],
                            "description": p_tags[9],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": h1_tags[2],
                            "description": p_tags[10],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": h1_tags[2],
                            "description": p_tags[11],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": h1_tags[2],
                            "description": p_tags[12],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": h1_tags[2],
                            "description": p_tags[13],
                            "created": created
                        }
                    ]
                    # add each dictionary entry to a list
                    # list will be combined with other lists
                    for i in event_list:
                        scraped_events.append(i)

                elif "Women's Climbing Symposium" in item[0]:
                    url = "https://www.womensclimbingsymposium.com/wcs23"
                    name = "Women's Climbing Symposium"

                    # retrive tag content from html, with extra tidies
                    h1_tags = self.search_tags_alternative('h1', soup)
                    h1_tag_list = []
                    for tag in h1_tags:
                        h1_tag_list.append(tag.replace("\n", " "))

                    p_tags = self.search_tags_alternative('p', soup)
                    p_tag_list = []
                    for tag in p_tags:
                        p_tag_list.append(tag.replace("\n\n", " "))

                    event_list = [
                        {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": h1_tag_list[0],
                            "subtitle": '',
                            "description": p_tag_list[6],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[8],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": '',
                            "description": p_tag_list[10],
                            "created": created
                        }
                    ]
                    for i in event_list:
                        scraped_events.append(i)

                elif "Speakers From The Edge" in item[0]:
                    url = "https://www.speakersfromtheedge.com/theatre-tours"
                    name = "Speakers from the Edge"

                    a_tags = self.search_tags_alternative('a', soup)
                    a_tags = self.strip_spaces_and_breaks(a_tags)
                    a_tags = self.remove_blanks(a_tags)
                    # remove duplicate tags
                    a_tags = list(dict.fromkeys(a_tags))

                    p_tags = self.search_tags_alternative('p', soup)
                    p_tags = self.strip_spaces_and_breaks(p_tags)
                    p_tags = self.remove_blanks(p_tags)

                    event_list = [
                        {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": a_tags[10],
                            "description": p_tags[0],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": a_tags[16],
                            "description": p_tags[1],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": a_tags[18],
                            "description": p_tags[2],
                            "created": created
                        }, {
                            "event": "event",
                            "name": name,
                            "url": url,
                            "intro": '',
                            "title": '',
                            "subtitle": a_tags[20],
                            "description": p_tags[3],
                            "created": created
                        }
                    ]
                    for i in event_list:
                        scraped_events.append(i)

                else:
                    print("None of these phrases found in the soup")

        # print output to check it came out correctly
        # for row in scraped_events:
        #    print(row)

        """send the compiled scraped events list to the database module,
        and append the result to the output list"""
        # output.append(db_conn.DatabaseConnection(scraped_events))
        # return output


# manually start up a new instance of this class
# this is exactly the same as when it is instantiated from flask_app.py
instance = Events()
instance.assign_values()
