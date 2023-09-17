from bs4 import BeautifulSoup
import requests
import json

url = "https://www.edenrockclimbing.com/adult-classes-carlisle"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

#h6 span - titles
#p span span - text


def find_h6():
    """search the html for <span> tags within <h6> tags and return the content as a list"""
    list_1 = []
    h6_tag = soup.find_all('h6')
    h6_tag = [e.string for e in h6_tag]
    return h6_tag


def find_p():
    """search the html for <span> tags within <p><span> tags and return the content as a list"""
    list_1 = []
    p_tag = soup.find_all('p')
    for e in p_tag:
        e = e.text
        list_1.append(e)
    return list_1


find_h6 = find_h6()
find_p = find_p()

'''for i in find_h6:
    print(i)

for j in find_p:
    print(j)
'''


edenRock_classes = {
    "name": "Eden Rock, Carlisle",
    "title_1": find_h6[0],
    "description_1": find_p[6],
    "title_2": find_h6[1],
    "description_2": find_p[9],
    "title_3": find_h6[2],
    "description_3": [find_p[12], find_p[14], find_p[16]],
    "title_4": find_h6[3],
    "description_4": find_p[18],
    "title_5": find_h6[4],
    "description_5": find_p[20],
    "title_6": find_h6[5],
    "description_6": find_p[23],
    "title_7": find_h6[6],
    "description_7": [find_p[26], find_p[28]],
    "url": "https://www.edenrockclimbing.com/adult-classes-carlisle"
}


"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(edenRock_classes, file, indent = 4)
        

