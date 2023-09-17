from bs4 import BeautifulSoup
import requests
import json

url = "https://www.madvolume.co.uk/climbing-classes/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_title():
    """search the html for <span> tags and return the content as a list"""
    list_1 = []
    span_tag = soup.find_all('span')
    span_tag_list = [e.string for e in span_tag]
    for p in span_tag_list:
        if p != "\xa0" and p != None:
            list_1.append(p)
    return(list_1)

def find_text():
    """search the html for <div> tags and return the content as a list"""
    list_1 = []
    div_tag = soup.find_all('div')
    div_tag_list = [e.string for e in div_tag]
    for p in div_tag_list:
        if p != "\xa0" and p != "\n" and p != None:
            list_1.append(p)
    return list_1

find_span = find_title()
find_text = find_text()

madvolume_classes = {
    "name": "Mad Volume, Hull",
    "title_1": find_span[3],
    "description_1": find_text[0],
    "title_2": find_span[5],
    "description_2": find_text[3],
    "title_3": find_span[8],
    "description_3": find_text[5],
    "url": "https://www.madvolume.co.uk/climbing-classes/"
}
    
    
"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(madvolume_classes, file, indent = 4)
