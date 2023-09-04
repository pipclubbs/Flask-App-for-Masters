from bs4 import BeautifulSoup
import requests
import json

url = "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/lessons-sessions/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def search_tags(tag):
    searched_soup = soup.find_all(tag)
    tag_list = [e.string for e in searched_soup]
    return tag_list


find_p = search_tags('p')
find_h2 = search_tags('h2')

lincoln_ymca_classes = {
    "name": "YMCA Lincolnshire, Lincoln",
    "title_1": find_h2[1],
    "description_1": [find_p[5], find_p[6]],
    "title_2": find_h2[2],
    "description_2": [find_p[7], find_p[8]],
    "title_3": find_h2[3],
    "description_3": [find_p[9], find_p[10]],
    "title_4": find_h2[4],
    "description_4": [find_p[11], find_p[12]],
    "title_5": find_h2[5],
    "description_5": [find_p[13], find_p[14]],
    "url": "https://www.lincsymca.co.uk/heath-wellbeing/climbing-bouldering/lessons-sessions/"
}    

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(lincoln_ymca_classes, file, indent = 4)
