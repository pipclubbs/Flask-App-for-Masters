"""Web scraper to gather class data from Climbing Works"""
from bs4 import BeautifulSoup
import requests
import json

url = "https://www.climbingworks.com/adult-classes"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def search_tags(tag):
    """Find all the tags of the type in the parameter on the page and return as a list"""
    list_1 = []
    searched_soup = soup.find_all(tag)
    tag_list = [e.string for e in searched_soup]
    for p in tag_list:
        if p != None and p != '\u200b':
            list_1.append(p)
    return list_1


find_p = search_tags('p')
find_span = search_tags('span')


climbingworks_classes = {
    "name": "The Climbing Works, Sheffield",
    "title_1": find_span[52],
    "description_1": [find_p[19], find_p[20]],
    "title_2": find_span[54],
    "description_2": [find_p[23], find_p[24]],
    "title_3": find_span[56],
    "description_3": [find_p[36], find_p[37]],
    "title_4": find_span[58],
    "description_4": [find_p[50], find_p[51]],
    "title_5": find_span[60],
    "description_5": [find_span[38], find_span[39], find_span[40]],
    "title_6": find_span[62],
    "description_6": [find_p[57], find_p[58], find_p[59]],
    "title_7": find_span[64],
    "description_7": find_span[48],
    "url": "https://www.climbingworks.com/adult-classes"
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(climbingworks_classes, file, indent=4)
