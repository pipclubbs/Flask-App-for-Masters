import db_conn2
from class_scrapers import ClassScraper


class NorthWestContacts(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        # chosen_area = area
        output = []
        scraped_centres = []
        centres = [
            {
                "name": "Eden Rock, Carlisle",
                "contactUrl": "https://www.edenrockclimbing.com/contact-carlisle",
                "homeUrl": "https://www.edenrockclimbing.com/carlisle-home"
            },
            {
                "name": "Blochaus Climbing, Manchester",
                "contactUrl": "",
                "homeUrl": ""
            }
        ]

        for c in centres:
            if c["name"] == "Eden Rock, Carlisle":
                contactUrl = c["contactUrl"]

                span_tags = self.search_tags('span', contactUrl)
                # print(span_tags)
                span_tags = [i for n, i in enumerate(
                    span_tags) if i not in span_tags[:n]]
                # for i, tag in enumerate(span_tags):
                #    print(i, tag)

                centre_details = [
                    {
                        "area": "north-west",
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
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)
                # for j in scraped_centres:
                 #   print(j)

        output.append(db_conn2.DatabaseConnection(scraped_centres))
        # for i in output:
        #    print(i)
        return output
