import re

p_tags = ['Mountaineering, rock climbing, hill walking and other mountain sports',
          '\nMenu\n',
          'CORONAVIRUS – March 2023',
          'Club activities are fully resumed, including Tuesday evening indoor climbing at Creation, day walks, social events, climbing trips and weekend camping and hut meets. We are now back to being our active, lively, sociable selves, and are hope to continue this for all 2023.\xa0',
          'Make Friends – Find Activity Partners – Gain Skills – Adventure Outdoors !\n\nSolihull Mountaineering Club welcomes rock climbers, mountaineers and hillwalkers from Solihull, Birmingham and across the West Midlands.\nWe are an active club, with a busy programme of weekends away, as well as social events, lectures and more.', 'Outdoor Mountaineering, Climbing and more!\nEvery month we have scheduled weekend meets, staying in mountaineering club cottages, bunkhouses or camping. We also have many day and social events organised,\xa0 and an enthusiastic network of members who arrange additional days out and weekends away.', 'Indoor Climbing\nWe climb indoors at Creation Climbing Centre, 582 Moseley Rd, Birmingham B12 9AA on Tuesday evenings.', 'Club members regularly go bouldering at The Depot, 10 Sherlock St, Birmingham B5 6LU and also at Birmingham Bouldering Centre,\xa0 2 Water St, Birmingham, B3 1HL.\n', 'Other Club Activities\nOther activities such as lectures, dinners and training events are often held at Old Edwardians Sports Club, Streetsbrook Road, Solihull, B90 3PE.', 'Climbing and mountaineering are activities with a danger of personal injury or death. Participants in these activities should be aware of and accept these risks and be responsible for their own actions.']
span_tags = ['Menu', 'Outdoors adventures with SMC - lead climbing on sea cliffs', "Classic rock climbs with SMC - the Devil's Slide on Lundy", 'Alpine climbing in the French Alps near Chamonix', 'Club members regularly go bouldering at The Depot, 10 Sherlock St, Birmingham B5 6LU and also at Birmingham Bouldering Centre,\xa0 2 Water St, Birmingham, B3 1HL.\n', '10 Sherlock St, Birmingham B5 6LU ', 'Pages', 'Recent Posts', 'Solihull Mountaineering Club', 'Spacious', 'WordPress']

p_tag_list = []
p_tags_updated = []
for tag in p_tags:
    p_tag_list.append(tag.replace("\n\n", ""))
for tag in p_tag_list:
    p_tags_updated.append(tag.replace("\n", ""))







print("p")
for i, tag in enumerate(p_tags_updated):
    print(i, tag)

print("span")
for i, tag in enumerate(span_tags):
    print(i, tag)

'''
club_list = [
    {
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[4]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[5]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[6]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[7]
    },{
        "intro": '',
        "title": '',
        "subtitle": '',
        "description": p_tags[8]
    }
]

#print(centre_details)
for line in club_list:
    for key, value in line.items():
        print(key, ":", value)'''
