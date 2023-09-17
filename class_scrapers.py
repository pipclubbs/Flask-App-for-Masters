from bs4 import BeautifulSoup
import requests
# import db_conn2


class ClassScraper:
    def __init__(self):
        self.name = ""
        self.url = ""
        self.title = ""
        self.description = ""

    def get_html(self, url):
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        return soup

    def search_tags(self, tag, url):
        url = url
        soup = self.get_html(url)
        searched_soup = soup.find_all(tag)
        tag_list = [e.string for e in searched_soup]
        return tag_list

    def search_tags_alternative(self, tag, url):
        url = url
        soup = self.get_html(url)
        tag_list = []
        tags = soup.find_all(tag)
        for e in tags:
            e = e.text
            tag_list.append(e)
        return tag_list

    def remove_blanks(self, list):
        new_list = []
        for i in list:
            if i != None:
                new_list.append(i)
        return new_list

    def do_join(self, list):
        list = list
        new_list = []
        for j in list:
            j = " ".join(j.split())
            new_list.append(j)
        return new_list
