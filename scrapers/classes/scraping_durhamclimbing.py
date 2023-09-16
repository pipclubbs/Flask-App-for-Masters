from bs4 import BeautifulSoup
import requests
import json

url = "https://www.durhamclimbingcentre.co.uk/coaching"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h2():
    """search the html for <h4> tags and return the content as a list"""
    list_1 = []
    h2_tag = soup.find_all('h2')
    h2_tag_list = [e.string for e in h2_tag]
    for t in h2_tag_list:
        t = " ".join(t.split())
        list_1.append(t)
    return list_1


def find_h3():
    """search the html for <h3> tags and return the content as a list"""
    list_1 = []
    list_2 = []
    h3_tag = soup.find_all('h3')
    h3_tag_list = [e.string for e in h3_tag]
    for p in h3_tag_list:
        if p != None:
            list_1.append(p)
    for t in list_1:
        t = " ".join(t.split())
        list_2.append(t)
    return list_2


def find_div():
    """search the html for <div> tags and return the content as a list"""
    list_1 = []
    list_2 = []
    div_tag = soup.find_all('div')
    div_tag_list = [e.string for e in div_tag]
    for p in div_tag_list:
        if p != None and "\xa0" not in p and "Contact Us" not in p and "Stay tuned" not in p:
            list_1.append(p)
    for t in list_1:
        t = " ".join(t.split())
        list_2.append(t)
    return list_2


def find_p():
    """search the html for <p> tags and return the content as a list"""
    list_1 = []
    p_tag = soup.find_all('p')
    for e in p_tag:
        e = e.text
        list_1.append(e)
    return list_1


def find_span():
    """search the html for <span> tags and return the content as a list"""
    list_1 = []
    span_tag = soup.find_all('span')
    span_tag_list = [e.string for e in span_tag]
    for p in span_tag_list:
        if p != None:
            list_1.append(p)
    return list_1


def find_li():
    """search the html for <li> tags and return the content as a list"""
    list_1 = []
    li_tag = soup.find_all('li')
    li_tag_list = [e.string for e in li_tag]
    for p in li_tag_list:
        if p != None:
            list_1.append(p)
    return list_1


find_h2 = find_h2()
find_h3 = find_h3()
find_div = find_div()
find_p = find_p()
find_span = find_span()
find_li = find_li()

durham_classes = {
    "name": "Durham Climbing Centre, Durham",
    "title_1": find_h3[0],
    "description_1": [find_div[0], find_p[0]],
    "title_2": find_h2[0],
    "description_2": [find_p[1], find_p[2], find_p[3]],
    "title_3": find_h2[1],
    "description_3": [find_div[10], find_p[5]],
    "title_4": find_h3[1],
    "description_4": [find_div[11], find_p[6], find_p[7]],
    "title_5": find_h2[2],
    "description_5": [find_div[12], find_p[8]],
    "url": "https://www.durhamclimbingcentre.co.uk/coaching"
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(durham_classes, file, indent=4)
