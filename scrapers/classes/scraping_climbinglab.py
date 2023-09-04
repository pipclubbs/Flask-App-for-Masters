from bs4 import BeautifulSoup
import requests
import json

url = "https://www.climbinglab.co.uk/your-visit-begin/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h3():
    h3_tag = soup.find_all('h3')
    h3_tag_list = [e.string for e in h3_tag]
    return h3_tag_list


def find_p():
    list_1 = []
    list_2 = []
    p_tag = soup.find_all('p')
    for e in p_tag:
        e = e.text
        list_1.append(e)
    for p in list_1:
        if p != "\xa0":
            list_2.append(p)
    return list_2


find_h3 = find_h3()
find_p = find_p()

climbinglab_classes = {
    "name": "The Climbing Lab, Leeds",
    "title_1": find_h3[1],
    "description_1": find_p[12],
    "title_2": find_h3[2],
    "description_2": [find_p[13], find_p[16]],
    "url": "https://www.climbinglab.co.uk/your-visit-begin/"
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(climbinglab_classes, file, indent = 4)
