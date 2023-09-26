import re
import db_conn2

from class_scrapers import ClassScraper


class Events(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        output = []
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

        for e in events:
            '''if e["name"] == "Brit Rock Film Tour":
                url = e["url"]
                soup = self.get_html(url)
                event = e["event"]

                h1_tags = self.search_tags_alternative('h1', soup)
                p_tags = self.search_tags_alternative('p', soup)
                p_tags = self.strip_spaces_and_breaks(p_tags)

                event_list = [
                    {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": p_tags[1],
                        "title": '',
                        "subtitle": '',
                        "description": "View web site for full event listings"
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[9]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[10]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[11]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[12]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[13]
                    }
                ]
                for i in event_list:
                    scraped_events.append(i)

            if e["name"] == "Women's Climbing Symposium":
                url = e["url"]
                soup = self.get_html(url)
                event = e["event"]

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
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": h1_tag_list[0],
                        "subtitle": '',
                        "description": p_tag_list[6]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tag_list[8]
                    }, {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": '',
                        "description": p_tag_list[10]
                    }
                ]
                for i in event_list:
                    scraped_events.append(i)'''

            if e["name"] == "Speakers from the Edge":
                url = e["url"]
                soup = self.get_html(url)
                event = e["event"]

                a_tags = self.search_tags_alternative('a', soup)
                a_tags = self.strip_spaces_and_breaks(a_tags)
                a_tags = self.remove_blanks(a_tags)
                a_tags = list(dict.fromkeys(a_tags))
                
                p_tags = self.search_tags_alternative('p', soup)
                p_tags = self.strip_spaces_and_breaks(p_tags)
                p_tags = self.remove_blanks(p_tags)

                event_list = [
                    {
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": a_tags[10],
                        "description": p_tags[0]
                    },{
                        "event": "event",    
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": a_tags[16],
                        "description": p_tags[1]
                    },{
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": a_tags[18],
                        "description": p_tags[2]
                    },{
                        "event": "event",
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": a_tags[20],
                        "description": p_tags[3]
                    }
                ]
                for i in event_list:
                    scraped_events.append(i)

        '''for row in scraped_events:
            for key, value in row.items():
                print(key, ":", value)'''

        output.append(db_conn2.DatabaseConnection(scraped_events))
        return output


#instance = Events()
#instance.assign_values()
