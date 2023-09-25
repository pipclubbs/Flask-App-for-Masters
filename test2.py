import re

p_tags = ['Home', 'Activities', 'Calendar', 'Trip Reports', 'Join Us', 'Blog', 'Contact Us', 'Links', "The Club's calendar of activities includes:", 'Our members will also be found taking part in mountain marathons, fell running, mountain biking, road biking, orienteering, and possibly even caving.', '']
td_tags = ["York Alpine Club was founded in 1981, and exists for the encouragement of all kinds of mountain activities, including walking, climbing, skiing and biking, and is affiliated to the BMC. We pride ourselves on being friendly and welcoming to new members, whatever your level of experience. The Club's calendar of activities includes: Weekend meets, staying in huts or camping Mid-week evening and weekend climbing, on local crags in the summer and at local climbing walls during the winter Regular social events Our members will also be found taking part in mountain marathons, fell running, mountain biking, road biking, orienteering, and possibly even caving. For more details see the Join Us page Check our blog to see what we have been up to recently. Latest Blog: Richard Payne Meet 2023 by Simon C [Thursday 16th March, 2023] As the 3-day Laggan meet grew near, were were treated to the traditional mega-thaw …", 'York Alpine Club was founded in 1981, and exists for the encouragement of all kinds of mountain activities, including walking, climbing, skiing and biking, and is affiliated to the BMC. We pride ourselves on being friendly and welcoming to new members, whatever your level of experience.', 'York Alpine Club was founded in 1981, and exists for the encouragement of all kinds of mountain activities, including walking, climbing, skiing and biking, and is affiliated to the BMC. We pride ourselves on being friendly and welcoming to new members, whatever your level of experience.', "The Club's calendar of activities includes: Weekend meets, staying in huts or camping Mid-week evening and weekend climbing, on local crags in the summer and at local climbing walls during the winter Regular social events Our members will also be found taking part in mountain marathons, fell running, mountain biking, road biking, orienteering, and possibly even caving. For more details see the Join Us page Check our blog to see what we have been up to recently.", '', '', 'Latest Blog: Richard Payne Meet 2023 by Simon C [Thursday 16th March, 2023] As the 3-day Laggan meet grew near, were were treated to the traditional mega-thaw …', 'Richard Payne Meet 2023 by Simon C [Thursday 16th March, 2023] As the 3-day Laggan meet grew near, were were treated to the traditional mega-thaw …', '', 'BMC Participation Statement', '', 'This site is maintained by Simon Caldwell All photos are by me unless otherwise credited']
li_tags = ['Weekend meets, staying in huts or camping', 'Mid-week evening and weekend climbing, on local crags in the summer and at local climbing walls during the winter', 'Regular social events']

'''p_tag_list = []
p_tags_updated = []
for tag in p_tags:
    p_tag_list.append(tag.replace("\n", ""))'''

for i, tag in enumerate(p_tags):
    print(i, tag)
    
print("td")
for i, tag in enumerate(td_tags):
    print(i, tag)

print("li")
for i, tag in enumerate(li_tags):
    print(i, tag)

'''print("h3")
for i, tag in enumerate(h3_tags):
    print(i, tag)'''

'''print("span")
for i, tag in enumerate(span_tags):
    print(i, tag)'''
    
'''
club_list = [
    {
        "intro": td_tags[2],
        "title": '',
        "subtitle": '',
        "description": td_tags[3]
    }
]

#print(centre_details)
for line in club_list:
    for key, value in line.items():
        print(key, ":", value)'''
