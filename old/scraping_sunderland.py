from bs4 import BeautifulSoup
import requests
import json

url = "https://sunderlandwall.com/courses/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h3():
    h3_tag = soup.find_all('h3')
    h3_tag_list = [e.string for e in h3_tag]
    return h3_tag_list



def find_h4():
    h4_tag = soup.find_all('h4')
    h4_tag_list = [e.string for e in h4_tag]
    return h4_tag_list
    

def find_p():
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    return p_tag_list




def find_li():
    list_1 = []
    list_2 = []
    list_3 = []
    li_tag = soup.find_all('li')
    for e in li_tag:
        e = e.text
        list_1.append(e)
    for p in list_1:
        if p != None:
            list_2.append(p)
    for t in list_2:
        if len(t) > 25:
            list_3.append(t)
    return list_3



find_h3 = find_h3()
find_h4 = find_h4()
find_p = find_p()
find_li = find_li()


sunderland_classes = {
    "name": "Sunderland Wall",
    "title_1": find_h3[0],
    "description_1": [find_p[1], find_li[6], find_li[7], find_li[8], find_li[9], find_li[10]],
    "title_2": find_h3[1],
    "description_2": [find_p[2], find_li[11], find_li[12], find_li[13], find_h4[0], find_p[3], find_h4[1], find_p[4]],
    "url": "https://sunderlandwall.com/courses/"
}

"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(sunderland_classes, file, indent = 4)
    
