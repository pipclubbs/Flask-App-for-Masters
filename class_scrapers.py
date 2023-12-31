"""parent class containing methods utilised by the child scraper classes"""
import re
import requests
import time
from bs4 import BeautifulSoup


class ClassScraper:
    """class containing the methods for the web scrapers"""

    def __init__(self):
        self.name = ""
        self.url = ""
        self.title = ""
        self.description = ""


    """method to request the html for the site and parse it
    using the Beautiful Soup module"""
    def get_html(self, url):
        try:
            result = requests.get(url, timeout=8)
            soup = BeautifulSoup(result.text, "html.parser")
        except requests.exceptions.Timeout:
            print(f"Timeout while scraping {url}")
            return None
        except requests.exceptions.ConnectionError:
            print(f"Connection error while scraping {url}")
            return None
        except Exception as e:
            print(f"Unexpected error while scraping {url}: {e}")
            return None
        finally:
            if result is not None:
                result.close()

        time_difference = time.time() - start_time
        print('Scraping time: %.2f seconds.' % time_difference)
        return soup

    
    """given the name of the tag and the html 'soup' to be searched, 
    return the contents of the tags as a list of strings"""
    def search_tags(self, tag, input_soup):
        searched_tag = tag
        soup = input_soup
        searched_soup = soup.find_all(searched_tag)
        tag_list = [e.string for e in searched_soup]
        return tag_list


    """alternative to the above method - for use when the 
    tag content contains other elements (such as <br>)"""
    def search_tags_alternative(self, tag, input_soup):
        searched_tag = tag
        soup = input_soup
        tag_list = []
        tags = soup.find_all(searched_tag)
        for e in tags:
            e = e.text
            tag_list.append(e)
        return tag_list


    """remove any None values from the list generated by the search"""
    def remove_blanks(self, input_list):
        new_list = []
        for i in input_list:
            if i is not None:
                new_list.append(i)
        return new_list


    """tidy the code: split into a list of single word strings, then 
    join them together as a single string of words separated by a space"""
    def do_join(self, input_list):
        new_list = []
        for j in input_list:
            j = " ".join(j.split())
            new_list.append(j)
        return new_list

    
    """removes excess spaces and linebreakss from the code"""
    def strip_spaces_and_breaks(self, data):
        input_list = data
        new_tag_list = []
        for tag in input_list:
            tag = re.sub(r'\s+', ' ', tag).strip()
            new_tag_list.append(tag)
        return new_tag_list

    
    """pulls emails and phone numbers from lists using regex"""
    def extract_contacts(self, string):
        # Define regular expressions for email address and phone number
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        phone_pattern = r'(\b\d{4} \d{3} \d{4}\b)|(\b\d{4} \d{7}\b)|(\b\d{5} \d{3} \d{3}\b)'

        # Find email addresses and phone numbers using re.findall
        email_addresses = re.findall(email_pattern, string)
        phone_numbers = re.findall(phone_pattern, string)

        # Extracted email addresses and phone numbers
        return [email_addresses, phone_numbers]


    """Split string into a list of strings, using the regex as the delimiter"""
    def split_string(self, string):
        string_list = re.sub(
            r'([a-z])([A-Z])', r'\1 \2', string)
        string_list = re.sub(r'(:)([A-Z])', r'\1 \2', string_list)
        string_list = re.sub(r'([a-z])([0-9])', r'\1 \2', string_list)
        string_list = re.sub(r'(,)([A-Z])', r' \2', string_list)
        words = string_list.split()
        word_list = ' '.join(words)
        word_list = re.split("\s+", word_list)
        return word_list
