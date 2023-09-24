data_dict = {'type': 'club', 'area': 'north-east', 'name': 'Durham Mountain Sports', 'url': 'https://durhammountainsports.org.uk/wp/about/', 'intro': '', 'title': '', 'subtitle': '', 'description': 'Activities often take place over the course of a weekend (particularly bank holidays), typically camping in the summer but using cottages, youth hostels, camping barns or walking huts in the winter. Popular venues include the Lake District, Yorkshire Dales, North Yorkshire Moors, Northumberland and Scotland.'}

if 'type' in data_dict:
    print(True)
else:
    print(False)






'''import re

p_tags = ["Get out and about with Durham's friendliest outdoor club!", 'We are the North East’s fastest growing multi-activity outdoor pursuits club that meets in Framwellgate Moor on the outskirts of Durham City. Our members are from all parts of the county and beyond and we’re always eager to welcome new members (who incidentally, must be over 18).', 'The club is affiliated to the\xa0BMC\xa0and is run by its members for its members. Within our ranks we have\xa0walkers,\xa0climbers,\xa0skiers\xa0and\xa0mountain-bikers\xa0representing every level of competence from highly experienced to complete beginner.', 'We aim to provide a friendly, supportive environment where experienced club members can pass on their skills or can recommend appropriate training.', 'Activities often take place over the course of a weekend (particularly bank holidays), typically camping in the summer but using cottages, youth hostels, camping barns or walking huts in the winter. Popular venues include the Lake District, Yorkshire Dales, North Yorkshire Moors, Northumberland and Scotland.', 'If you love the outdoors and want to make lots of new friends who have similar interests, come along and meet us. However, if you find the prospect of turning up knowing no-one daunting, then why not contact us first? Check out our contact page. ']
print("p")
for i, tag in enumerate(p_tags):
    print(i, tag)

print("H2")
for i, tag in enumerate(h2_tags):
    print(i, tag)

print("p")
for i, tag in enumerate(p_tags):
    print(i, tag)


club_list = [
    {
        "intro": p_tags[0],
        "title": '',
        "subtitle": '',
        "description": p_tags[1]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[2]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[3]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[4]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[5]
    }
]

#print(centre_details)
for line in centre_details:
    for key, value in line.items():
        print(key, ":", value)'''
