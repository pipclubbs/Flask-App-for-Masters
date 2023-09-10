from bs4 import BeautifulSoup
import requests
import json
import pprint
import sqlite

url = "https://www.ibexbouldering.co.uk/copy-of-classes-1"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h2():
    list_1 = []
    list_2 = []
    h2_tag = soup.find_all('h2')
    for e in h2_tag:
        e = e.text
        list_1.append(e)
    for t in list_1:
        t = " ".join(t.split())
        list_2.append(t)
    return list_2


def find_h4():
    h4_tag = soup.find_all('h4')
    h4_tag_list = [e.string for e in h4_tag]
    return h4_tag_list


def find_p():
    list_1 = []
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    for p in p_tag_list:
        if p != '\u200b':
            list_1.append(p)
    return list_1


find_h2 = find_h2()
find_h4 = find_h4()
find_p = find_p()


ibex_classes = [
    {"name": "Ibex Bouldering, Darlington"},
    {"url": "https://www.ibexbouldering.co.uk/copy-of-classes-1"},
    {"title": find_h2[2],
     "description": [find_p[2], find_p[3], find_p[4], find_p[5], find_p[6], find_p[7], find_p[8]]},
    {"title": find_h2[3],
     "description": [find_p[12], find_p[13], find_p[14], find_p[15]]},
    {"title": find_h4,
     "description": [find_p[16], find_p[17], find_p[18], find_p[19], find_p[20]]},
    {"title": find_h2[4],
     "description": [find_h2[6], find_h2[7]]}

]

# print(ibex_classes)


def print_classes(centre):
    for i in centre:
        for values in i.values():
            if values == type(list):
                for j in values:
                    print(*j, sep="\n")
            else:
                print(values)
            


print_classes(ibex_classes)
'''
"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(ibex_classes, file, indent=4)
'''
