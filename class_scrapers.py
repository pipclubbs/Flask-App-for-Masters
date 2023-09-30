"""parent class containing the methods that are utilised by 
the child scraper classes"""

import re
from bs4 import BeautifulSoup
import requests
import time


class ClassScraper:
    """class containing the methods for the web scrapers"""

    def __init__(self):
        self.name = ""
        self.url = ""
        self.title = ""
        self.description = ""

    def get_html(self, url):
        """method to request the html for the site and parse it
        using the Beautiful Soup module"""
        start_time = time.time()

        result = requests.get(url, timeout=8)
        soup = BeautifulSoup(result.text, "html.parser")

        time_difference = time.time() - start_time
        print(f'Scraping time: %.2f seconds.' % time_difference)
        return soup

    def search_tags(self, tag, input_soup):
        """given the name of the tag and the html 'soup' to be 
        searched, return the contents of the tags as a 
        list of strings"""
        searched_tag = tag
        soup = input_soup
        searched_soup = soup.find_all(searched_tag)
        tag_list = [e.string for e in searched_soup]
        return tag_list

    def search_tags_alternative(self, tag, input_soup):
        """alternative to the above method - for use when the 
        tag content contains other elements (such as <br>)"""
        searched_tag = tag
        soup = input_soup
        tag_list = []
        tags = soup.find_all(searched_tag)
        for e in tags:
            e = e.text
            tag_list.append(e)
        return tag_list

    def remove_blanks(self, input_list):
        """remove any None values from the list generated
        by the tag search"""
        new_list = []
        for i in input_list:
            if i is not None:
                new_list.append(i)
        return new_list

    def do_join(self, input_list):
        """tidy the code by splitting it into a list of 
        single word strings, then joining them together
        as a single string of words separated by a space"""
        new_list = []
        for j in input_list:
            j = " ".join(j.split())
            new_list.append(j)
        return new_list

    def strip_spaces_and_breaks(self, data):
        """removes excess spaces and linebreakss from the code"""
        input_list = data
        new_tag_list = []
        for tag in input_list:
            tag = re.sub(r'\s+', ' ', tag).strip()
            new_tag_list.append(tag)
        return new_tag_list

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
