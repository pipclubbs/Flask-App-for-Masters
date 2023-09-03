from bs4 import BeautifulSoup
import requests
import json

"""This script requests the html for the classes page at Climb Newcastle,
and returns the relevant sorted scraped data to a json file""" 

url = "https://www.climbnewcastle.com/index.php?route=extension/cn/essentials"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

def find_h1():
    """search the html for an <h1> tag and return the content"""
    h1_tag = soup.find('h1')
    h1_tag = h1_tag.string
    return h1_tag


def find_h4():
    """search the html for <h4> tags and return the content as a list"""
    h4_tag = soup.find_all('h4')
    h4_tag_list = [e.string for e in h4_tag]
    return h4_tag_list


def final_p_list(p_tags):
    p_tags = p_tags
    list_1 = []
    for p in p_tags:
        if p != None and "shopping cart" not in p and "Climb Newcastle Ltd" not in p and "Pick a date" not in p:
            list_1.append(p)
    return list_1
        

def find_p():
    """search the html for <p> tags and return the content as a list
    to another function that will remove unnecessary list items"""
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    return final_p_list(p_tag_list)

"""run the functions above and assign the returned values to a dictionary"""    
find_h1 = find_h1()
find_h4 = find_h4()
find_p = find_p()

valley_classes = {
    "venue": "Climb Valley, Newcastle",
    "title": find_h1,
    "description_1": find_p[0],
    "class_title_1": find_h4[0],
    "description_2": find_p[1],
    "class_title_2": find_h4[1],
    "description_3": find_p[2],
    "session_title": find_h4[2],
    "session_details": [find_p[3], find_p[4], find_p[5]],
    "url": url
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(valley_classes, file, indent = 4)

