import re
import db_conn
from class_scrapers import ClassScraper


class MidlandsContacts(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        # chosen_area = area
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
                        "phone": p_tags_phone[1][0][2]
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)

        output.append(db_conn.DatabaseConnection(scraped_centres))
        return output

    def extract_contacts(self, string):
        # Define regular expressions for email address and phone number
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        phone_pattern = r'(\b\d{4} \d{3} \d{4}\b)|(\b\d{4} \d{7}\b)|(\b\d{5} \d{3} \d{3}\b)'

        # Find email addresses and phone numbers using re.findall
        email_addresses = re.findall(email_pattern, string)
        phone_numbers = re.findall(phone_pattern, string)

        # Extracted email addresses and phone numbers
        return [email_addresses, phone_numbers]

    def split_string(self, string):
        # Split the string into a list of strings, using the regular expression as the delimiter.
        string_list = re.sub(
            r'([a-z])([A-Z])', r'\1 \2', string)
        string_list = re.sub(r'(:)([A-Z])', r'\1 \2', string_list)
        string_list = re.sub(r'([a-z])([0-9])', r'\1 \2', string_list)
        string_list = re.sub(r'(,)([A-Z])', r' \2', string_list)
        words = string_list.split()
        word_list = ' '.join(words)

        word_list = re.split("\s+", word_list)
        # Remove any empty strings from the list.
        # string_list = [word for word in string_list if word]

        return word_list
