from bs4 import BeautifulSoup
import requests
import json

url = "https://www.foundryclimbing.com/adult-climbing"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_p():
    """search the html for <p> tags and return the content as a list"""
    list_1 = []
    p_tag = soup.find_all('p')
    for e in p_tag:
        e = e.text
        list_1.append(e)
    return list_1


find_p = find_p()

foundry_classes = {
    "name": "The Foundry, Sheffield",
    "title_1": find_p[0],
    "description_1": [find_p[4], find_p[5]],
    "title_2": find_p[6],
    "description_2": [find_p[8], find_p[10], find_p[11], find_p[12]],
    "title_3": find_p[13],
    "description_3": [find_p[15], find_p[19], find_p[20]],
    "title_4": find_p[27],
    "description_4": [find_p[31], find_p[33], find_p[34]],
    "url": "https://www.foundryclimbing.com/adult-climbing"
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(foundry_classes, file, indent=4)
