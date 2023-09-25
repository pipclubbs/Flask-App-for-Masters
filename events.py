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
            }
        ]

        for e in events:
            if e["name"] == "Brit Rock Film Tour":
                url = e["url"]
                soup = self.get_html(url)

                h1_tags = self.search_tags_alternative('h1', soup)
                p_tags = self.search_tags_alternative('p', soup)
                p_tags = self.strip_spaces_and_breaks(p_tags)

                event_list = [
                    {
                        "name": e["name"],
                        "url": url,
                        "intro": p_tags[1],
                        "title": '',
                        "subtitle": '',
                        "description": "View web site for full event listings"
                    }, {
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[9]
                    }, {
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[10]
                    }, {
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[11]
                    }, {
                        "name": e["name"],
                        "url": url,
                        "intro": '',
                        "title": '',
                        "subtitle": h1_tags[2],
                        "description": p_tags[12]
                    }, {
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

        for row in scraped_events:
            for key, value in row.items():
                print(key, ":", value)


instance = Events()
instance.assign_values()
