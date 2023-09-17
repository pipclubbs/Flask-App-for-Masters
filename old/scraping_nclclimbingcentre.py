from bs4 import BeautifulSoup
import requests
import json

url = "https://www.newcastleclimbingcentre.co.uk/courses/indoor-courses/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")


def find_h2():
    """search the html for <h2> tags and return the content as a list"""
    h2_tag = soup.find_all('h2')
    h2_tag_list = [e.string for e in h2_tag]
    return h2_tag_list


def final_span_list(span_tags):
    span_tags = span_tags
    list_1 = []
    for p in span_tags:
        if p != None and "Facebook" not in p and "Twitter" not in p and "Instagram" not in p and "Book online" not in p and "Select Page" not in p:
            list_1.append(p)
    return list_1


def find_span():
    """search the html for <span> tags and return the content as a list"""
    span_tag = soup.find_all('span')
    span_tag_list = [e.string for e in span_tag]
    return final_span_list(span_tag_list)


def final_p_list(p_tags):
    p_tags = p_tags
    list_1 = []
    for p in p_tags:
        if p != None and "Book online" not in p and "Select page" not in p and "Please note that" not in p:
            list_1.append(p)
    return list_1


def find_p():
    """search the html for <p> tags and return the content as a list"""
    p_tag = soup.find_all('p')
    p_tag_list = [e.string for e in p_tag]
    return final_p_list(p_tag_list)


def find_div():
    list_1 = []
    div_tag = soup.find_all('div')
    div_tag_list = [e.string for e in div_tag]
    for p in div_tag_list:
        if p != None and "Indoor Courses" not in p and "Our Friends and Sponsors" not in p and "\xa0" not in p:
            list_1.append(p)
    return list_1


def find_strong():
    list_1 = []
    strong_tag = soup.find_all('strong')
    strong_tag_list = [e.string for e in strong_tag]
    for p in strong_tag_list:
        if p != None:
            list_1.append(p)
    return list_1
    
            

find_h2 = find_h2()
find_span = find_span()
find_p = find_p()
find_div = find_div()
find_strong = find_strong()

climbNcl_classes = {
    "venue": "Climb Newcastle, Byker",
    "title_1": find_h2[0],
    "description_1": [find_p[0], find_p[1]],
    "title_2": find_h2[1],
    "description_2": [find_p[2], find_p[3], find_p[4], find_span[0], find_span[1], find_span[2], find_span[3], find_span[4], find_p[5]],
    "title_3": find_h2[2],
    "description_3": [find_p[6], find_p[7], find_p[8], find_p[9], find_p[10]],
    "title_4": find_h2[3],
    "description_4": [find_div[0], find_div[1], find_p[11], find_p[12], find_p[13]],
    "title_5": find_h2[4],
    "description_5": [find_p[14], find_p[15], find_strong[3]],
    "title_6": find_h2[5],
    "description_6": [find_p[16], find_p[17], find_p[18], find_p[19], find_p[20], find_p[21]],
    "title_7": find_h2[6],
    "description_7": [find_p[22], find_p[23], find_p[24]],
    "note": find_div[3],
    "url": "https://www.newcastleclimbingcentre.co.uk/courses/indoor-courses/"
}


"""convert dictionary to json and append to external json file"""
with open("saved_classes.json", "a") as file:
    json.dump(climbNcl_classes, file, indent = 4)
