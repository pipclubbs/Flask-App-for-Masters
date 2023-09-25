import re

p_tags = ['Watch the trailer', 'The BRIT ROCK FILM TOUR is back for 2023 with another stunning line-up of the UK’s best climbing and adventure films. Five exhilarating films capturing an array of hardcore action, pioneering spirit and some proper madness. The once again kicks off in Sheffield on Tues, 7th Nov followed by numerous dates across the UK. The online streaming window runs from 9-13th Nov.', "7th Nov: Auditorium, Sheffield Students' Union, Sheffield - WORLD PREMIERE 7th Nov: Dublin University Climbing Club, Dublin 8th Nov: UHI, Perth 9th Nov: Swansea University Mountaineering Club, Swansea 9th Nov: Bath University Mountaineering Club, Bath 9th Nov: Highland Cinema, Fort William 10th Nov: Parthian Climbing, Reading 10th Nov: Deckchair Cinema, Croyde 10th Nov: Kerry Climbing, Killorglin, Ireland 10th Nov: Plas Y Brenin, Capel Curig 10th Nov: Blocfit, London 10th Nov: The Warehouse, Gloucester 11th Nov: Nottingham Climbing Centre, Nottingham 11th Nov: Boulders, Cheltenham 11th Nov 15th Nov: Exeter Phoenix, Exeter 11th Nov: Rock & Snow, New York 11th Nov: Blochaus, Manchester 14th Nov: Gothenburg Climbing Club, Gothenburg, Sweden 14th Nov: Queens University Mountaineering Club, Belfast 15th Nov: NTNUI Tindegruppa, Trondheim, Norway 16th Nov: Queen's Hall, Hexham 17th Nov: Alaska Alpine Club, Fairbanks, Alaska 18th Nov: Mile End, London 18th Nov: The Tide Climbing Centre, Wadebridge 18th Nov: Boulders, Cardiff 18th Nov: Substation, Macclesfield 21st Nov: State Climb, Culpeper, Virginia, USA 23rd Nov: Kendal Mountain Festival, Kendal (presented by Alastair Lee) 23rd Nov: Cambridge Mountaineering Society, Cambridge 24th Nov: Substation, London 24th Nov: Strathearn Arts, Crieff 29th Nov: Lancashire Climbing and Caving Club, Bradshaw Conservative Club, Bolton 29th Nov: Grub, Manchester (presented by Alastair Lee) 1st Dec: Dirt Bag Corp, Golden, BC, Canada 1st Dec: University Of Cumbria, Ambleside 2nd Dec: The Project Climbing Centre, Poole 3rd Dec: Drill Hall, Chepstow 5th Dec: The Maynard, Grindleford 9th Dec: The Castle, London 20th Jan: Rheged, Penrith (presented by Alastair Lee) 15th Feb: The Barn, Aberdeenshire", 'Thanks for your interest in hosting the Brit Rock Film Tour.', 'Putting on a show is easy all you need is a suitable venue (with seating, projection and sound equipment), you pay a licence fee, promote and sell tickets then get ready to rock the crowd with the amazing line up of Brit Rock films.', 'Typical venues include climbing walls, outdoor retailers, community halls & theatres as well as mountaineering clubs, fundraising events and students unions. All grass roots locations linked with the outdoor world as well as traditional cinemas.', "We'll supply you with the master files/disks to play the films as well as provide stunning high-resolution artwork to help you promote your event.", "Local sponsors are a great way to help cover the licence fee as long as they don't clash with our lead sponsors.", 'Booking enquires: contact Matt Heason', "GODDESS OF CRAIC This film tells the story of rising trad star Freja Shannon. We join half-Swedish, half-Irish Freja in her ancestral homelands as she pursues her climbing goals for the season – ‘Sista Bossen’ E8 6c at the world-class granite climbing area of Bohuslan, Sweden and ‘Snell’s Law’ E7 6c at the Burren on the west coast of Ireland. Freja is as affable as she is committed once on the lead, resulting in captivating and gripping footage that will leave your jaw on the floor. The film also delves into Freja’s past, where we learn of her less-than-glamorous journey to becoming a professional climber – and how she overcame her inner doubts to break through as a leading female trad climber and alpinist. Whippers, sends and Nordic power screams all-inclusive in this spectacular and entertaining film. 'Goddess of Craic' 25mins", "SHINING STONES Climber Robbie Phillips chances upon a little-known mountain in the very far north of Scotland whilst driving from east coast to west. After some research, Robbie discovers the mountain is called Ben Loyal, and that climbing legend Simon Nadin has been developing a couple of lines at the crag. Simon tells him that there is something very special up there… What Robbie finds at Ben Loyal is off the scale: endless bouldering, highballs, countless quality granite tors and buttresses with untapped climbing potential. But all this pales into insignificance compared with the main face, which holds the future of trad climbing on what is surely one of Britain’s greatest cliffs. A truly stunning film of hard new routing by Robbie and Simon in an extraordinary setting. 'Shining Stones' 25mins", "HELMCKEN FALLS Emma Powell and Neil Gresham join the original pioneers of this unique ice climbing venue in British Columbia, Tim Emmett and Klemen ‘Klem’ Premrl once again push the boundaries of steep, sporty ice. After years of teasing, Tim finally invites his life-long friend Neil Gresham, along with top mixed climber Emma Powell to stoke up their pioneering spirit and develop some new lines at this surreal venue. 'Helmcken Falls' 15mins", "HARD GIT Controversial and never far from the news; climber Matt Wright goes trailblazing across the UK, making wild first ascents, hard solos and bold new lines. Loveable rogue and working-class hero Matt puts his money where his mouth is in this tour-de-force of hard climbing. After weighing up his time-verses-routes equation, Matt abandons an attempt of the infamous Rhapsody (E11) and sets off on a quest to climb new inspiring lines. He does not disappoint, with his energetic journey culminating in the first ascent of ‘Magical Thinking’ E10 7a – a heart-stoppingly dangerous route at Pavey Ark, Lake District. 'Hard Git' 20mins", "HEAD JAM Filmmaker Alastair Lee turns the camera on himself in this deep introspective story of triumph through adversity. Perceived as a successful man with the perfect life, Al experiences unexpectedly dark times. Fearing he will lose everything, we watch a man on the brink claw his way from despair, using climbing and training to find peace and salvation. Having never been the greatest of climbers, Al demolishes his inner punter – attempting to fulfil his potential by setting his sights on routes he’s spent 30 years avoiding. Includes hard first ascents, calamitous trad leads and bold on sights. Carnage ensues almost every time Al sets off on a lead in this gripping, hilarious, emotional and ultimately inspiring story of a man in struggle as he seeks to reconnect with himself. Adding to the riotous flavour of this production, Al asks the climbers he’s working with to do the filming. 'Headjam' 35mins", 'Total running time 120 mins', 'Tel: (+44) (0)1282 786716', 'Email us directly']
h1_tags = ['Tour', 'Host a Show', 'Films', 'Contact']


'''p_tag_list = []
p_tags_updated = []
for tag in p_tags:
    p_tag_list.append(tag.replace("\n", ""))'''


    
print("h1")
for i, tag in enumerate(h1_tags):
    print(i, tag)

print("p")
for i, tag in enumerate(p_tags):
    print(i, tag)

'''print("li")
for i, tag in enumerate(li_tags):
    print(i, tag)
'''
'''print("h3")
for i, tag in enumerate(h3_tags):
    print(i, tag)'''

'''print("span")
for i, tag in enumerate(span_tags):
    print(i, tag)'''
    

event_list = [
    {
        "name": e["name"],
        "url": url,
        "intro": p_tags[1],
        "title": '',
        "subtitle": '',
        "description": "View web site for full event listings"
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[2],
        "description": p_tags[9]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[2],
        "description": p_tags[10]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[2],
        "description": p_tags[11]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[2],
        "description": p_tags[12]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[2],
        "description": p_tags[13]
    }
]

#print(centre_details)
for line in event_list:
    for key, value in line.items():
        print(key, ":", value)
