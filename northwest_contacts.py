import db_conn
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
                soup = self.get_html(contactUrl)

                span_tags = self.search_tags('span', soup)
                # print(span_tags)
                span_tags = [i for n, i in enumerate(
                    span_tags) if i not in span_tags[:n]]
                # for i, tag in enumerate(span_tags):
                #    print(i, tag)

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
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)
                # for j in scraped_centres:
                 #   print(j)

            if c["name"] == "Blochaus Climbing, Manchester":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                p_tags = self.search_tags('p', soup)
                # print(f'p_tags: {p_tags}')

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
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)

        output.append(db_conn.DatabaseConnection(scraped_centres))
        # for i in output:
        #    print(i)
        return output

# instance = NorthWestContacts()
# instance.assign_values()
