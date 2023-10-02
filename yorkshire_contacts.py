import datetime
import re
import db_conn
from class_scrapers import ClassScraper


class YorkshireContacts(ClassScraper):
    def __init__(self):
        super().__init__()

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
            if c["name"] == "The Foundry, Sheffield":
                contactUrl = c["contactUrl"]
                area = c["area"]
                soup = self.get_html(contactUrl)

                if soup:
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

    def tidy_tags(self, list):
        new_list = []
        for i in list:
            if i != '\xa0' and i != '\n':
                new_list.append(i)
        return new_list
