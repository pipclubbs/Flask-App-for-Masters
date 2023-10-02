import datetime
import db_conn
from class_scrapers import ClassScraper


class MidlandsContacts(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        # chosen_area = area
        created = datetime.datetime.now()
        output = []
        scraped_centres = []
        centres = [
            {
                "area": "midlands",
                "name": "YMCA Lincolnshire, Lincoln",
                "contactUrl": "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/",
                "homeUrl": "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/"
            }
        ]

        for c in centres:
            if c["name"] == "YMCA Lincolnshire, Lincoln":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                if soup:
                    p_tags = self.search_tags_alternative('p', soup)
                    p_tags_address_list = self.split_string(p_tags[15])
                    p_tags_phone = self.extract_contacts(p_tags[12])
                    p_tags_email = self.extract_contacts(p_tags[13])

                    centre_details = [
                        {
                            "area": area,
                            "name": c["name"],
                            "homeUrl": c["homeUrl"],
                            "contactUrl": contactUrl,
                            "classUrl": '',
                            "street": f'{p_tags_address_list[0]} {p_tags_address_list[1]}',
                            "street_area": f'{p_tags_address_list[2]} {p_tags_address_list[3]}',
                            "city": p_tags_address_list[4],
                            "postcode": f'{p_tags_address_list[5]} {p_tags_address_list[6]}',
                            "email": p_tags_email[0][0],
                            "phone": p_tags_phone[1][0][2],
                            "created": created
                        }
                    ]
                    for i in centre_details:
                        scraped_centres.append(i)

                else:
                    pass

        output.append(db_conn.DatabaseConnection(scraped_centres))
        return output
