import re
import datetime
import db_conn
from class_scrapers import ClassScraper


class NorthEastContacts(ClassScraper):
    def __init__(self):
        super().__init__()

    def assign_values(self):
        created = datetime.datetime.now()
        output = []
        scraped_centres = []
        centres = [
            {
                "area": "north-east",
                "name": "Climb Valley, Newcastle",
                "contactUrl": "https://www.climbnewcastle.com/index.php?route=extension/cn/valley_travel",
                "homeUrl": "https://www.climbnewcastle.com"
            },
            {
                "area": "north-east",
                "name": "Durham Climbing Centre, Durham",
                "contactUrl": "https://www.durhamclimbingcentre.co.uk/contact",
                "homeUrl": "https://www.durhamclimbingcentre.co.uk/"
            },
            {
                "area": "north-east",
                "name": "Sunderland Wall, Sunderland",
                "contactUrl": "https://sunderlandwall.com/contact-us/",
                "homeUrl": "https://sunderlandwall.com/"
            },
            {
                "area": "north-east",
                "name": "Newcastle Climbing Centre, Byker",
                "contactUrl": "https://www.newcastleclimbingcentre.co.uk/contact-us/",
                "homeUrl": "https://www.newcastleclimbingcentre.co.uk/"
            }
        ]

        for c in centres:
            if c["name"] == "Climb Valley, Newcastle":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                p_tags = self.search_tags_alternative('p', soup)
                p_tags_address_list = self.split_string(p_tags[3])
                p_tags_contacts_list = self.extract_contacts(p_tags[24])

                centre_details = [
                    {
                        "area": area,
                        "name": c["name"],
                        "homeUrl": c["homeUrl"],
                        "contactUrl": contactUrl,
                        "classUrl": '',
                        "street": f'{p_tags_address_list[5]} {p_tags_address_list[6]}',
                        "street_area": '',
                        "city": f'{p_tags_address_list[7]} {p_tags_address_list[8]} {p_tags_address_list[9]}',
                        "postcode": f'{p_tags_address_list[10]} {p_tags_address_list[11]}',
                        "email": p_tags_contacts_list[0][0],
                        "phone": p_tags_contacts_list[1][0][0],
                        "created": created
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)
                # for j in scraped_centres:
                #    print(j)

            if c["name"] == "Durham Climbing Centre, Durham":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                li_tags = self.search_tags_alternative('li', soup)
                li_tags_address_list = self.split_string(li_tags[0])
                li_tags_phone = self.extract_contacts(li_tags[1])

                centre_details = [
                    {
                        "area": area,
                        "name": c["name"],
                        "homeUrl": c["homeUrl"],
                        "contactUrl": contactUrl,
                        "classUrl": '',
                        "street": f'{li_tags_address_list[0]} {li_tags_address_list[1]} {li_tags_address_list[2]}',
                        "street_area": f'{li_tags_address_list[3]} {li_tags_address_list[4]} {li_tags_address_list[5]}',
                        "city": li_tags_address_list[6],
                        "postcode": f'{li_tags_address_list[9]} {li_tags_address_list[10]}',
                        "email": "Please visit website directly for email address",
                        "phone": li_tags_phone[1][0][0],
                        "created": created
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)

            if c["name"] == "Sunderland Wall, Sunderland":
                homeUrl = c["homeUrl"]
                area = c["area"]
                soup = self.get_html("https://sunderlandwall.com/home/")

                p_tags_address = []
                p_tags = self.search_tags_alternative('p', soup)
                p_tags_contacts = self.extract_contacts(p_tags[2])
                p_tags_address = re.sub(r'(,)([A-Z])', r' \2', p_tags[3])
                p_tags_address = re.split("\s+", p_tags_address)

                centre_details = [
                    {
                        "area": area,
                        "name": c["name"],
                        "homeUrl": homeUrl,
                        "contactUrl": c["contactUrl"],
                        "classUrl": '',
                        "street": f'{p_tags_address[2]} {p_tags_address[3]}',
                        "street_area": f'{p_tags_address[4]} {p_tags_address[5]}',
                        "city": p_tags_address[0],
                        "postcode": f'{p_tags_address[6]} {p_tags_address[7]}',
                        "email": p_tags_contacts[0][0],
                        "phone": p_tags_contacts[1][0][1],
                        "created": created
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)

            if c["name"] == "Newcastle Climbing Centre, Byker":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                p_tags = self.search_tags_alternative(
                    'p', soup)
                p_tags_address_list = self.split_string(p_tags[1])
                p_tags_contact_list = self.extract_contacts(p_tags[2])

                centre_details = [
                    {
                        "area": area,
                        "name": c["name"],
                        "homeUrl": c["homeUrl"],
                        "contactUrl": contactUrl,
                        "classUrl": '',
                        "street": f'{p_tags_address_list[3]} {p_tags_address_list[4]} {p_tags_address_list[5]}',
                        "street_area": f'{p_tags_address_list[6]} {p_tags_address_list[7]} {p_tags_address_list[8]}',
                        "city": f'{p_tags_address_list[9]} {p_tags_address_list[10]} {p_tags_address_list[11]}',
                        "postcode": f'{p_tags_address_list[12]} {p_tags_address_list[13]}',
                        "email": p_tags_contact_list[0][0],
                        "phone": p_tags_contact_list[1][0][0],
                        "created": created
                    }
                ]
                for i in centre_details:
                    scraped_centres.append(i)

        '''for line in scraped_centres:
            for key, value in line.items():
                print(key, ":", value)'''
        # print(scraped_centres)
        output.append(db_conn.DatabaseConnection(scraped_centres))
        # for i in output:
        #    print(i)
        return output

    def extract_contacts(self, string):
        # Define regular expressions for email address and phone number
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        phone_pattern = r'(\b\d{4} \d{3} \d{4}\b)|(\b\d{4} \d{7}\b)'

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
        words = string_list.split()
        word_list = ' '.join(words)

        word_list = re.split("\s+", word_list)
        # Remove any empty strings from the list.
        # string_list = [word for word in string_list if word]

        return word_list
