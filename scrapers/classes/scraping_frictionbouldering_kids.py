from bs4 import BeautifulSoup
import requests
import json

url = "https://www.frictionbouldering.co.uk/kids"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())

def find_h2():
    """search the html for an <h2> tag and return the content"""
    h2_tag = soup.find('h2')
    h2_tag = h2_tag.string
    h2_tag = h2_tag.lower() # this content is in full caps on the webpage
    h2_tag = h2_tag.title()
    return h2_tag


def final_p_list(p_tags):
    """remove unnecessary items from list"""
    p_tags = p_tags
    list_1 = []
    for p in p_tags:
        if p != None:
            list_1.append(p)
    return list_1


def find_p():
    """search the html for <p> tags and return the content as a list
    to another function that will remove unnecessary list items"""
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    return final_p_list(p_tag_list)

"""run the functions above and assign the returned values to a dictionary"""
find_h2 = find_h2()
find_p = find_p()

friction_kids_classes = {
    "venue": "Friction (Gateshead)",
    "title": find_h2,
    "description": [find_p[0], find_p[1], find_p[2]],
    "url": url
}

"""convert dictionary to json and append to external json file"""
with open("saved_kids_classes.json", "a") as file:
    json.dump(friction_kids_classes, file, indent = 4)

