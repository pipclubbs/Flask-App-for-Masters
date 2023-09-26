import re

a_tags = ['', '', 'Home', 'Our speakers', 'Talent representation', 'Tours', 'About Us', 'Blog', 'Contact us', 'Menu', '', '', '', 'Home', 'Our speakers', 'Talent representation', 'Tours', 'About Us', 'Blog', 'Contact us', '', 'Oct 3 to Oct 27', 'Martyn Ashton - Bike Party', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Jan 24 to Feb 3', 'Karen Darke MBE & Steve Bate MBE - Wild Tracks', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Feb 6 to Feb 29', 'Pete Whittaker - Fine Lines', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Mar 5 to Mar 30', 'Hans Rey - Mishaps & Mayhem', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Sep 2 to Sep 24', 'Hazel Findlay - The Walls Within', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Jun 2 to Jun 25', 'Kenton Cool - Everest: The Untold Story', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Mar 23 to Apr 23', "James Ketchell - It's All Mental", '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Feb 1 to Feb 27', 'Mark Beaumont - Faster', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Sep 30 to Oct 27', 'Leo Houlding - Closer to the Edge', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Sep 13 to Sep 30', 'Adrian Hayes - To the Ends of the Earth', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Mar 16 to Apr 15', 'Stephen Venables - Life After Everest', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Feb 22 to Mar 3', 'Pete Whittaker - Solo & Free', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Oct 24 to Nov 22', 'Andy Kirkpatrick - Mind Your Head: Holidays from Hell', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Sep 9 to Oct 9', 'Kenton Cool - Everest the Cool Way', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Mar 9 to Mar 31', 'Pete Whittaker - Solo and Free', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Feb 21 to Mar 4', 'Athletes', 'Adventurers', 'Mark Beaumont - Around the World in 80 Days', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Feb 4 to Feb 14', 'Athletes', 'Tours', 'Sasha DiGiulian - Beyond the Comfort Zone', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Nov 27 to Dec 5', 'Mountaineers', 'Sir Chris Bonington – Life and Times', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Nov 2 to Nov 17', 'Adventurers', 'James Ketchell - Chasing Extremes', 'Google Calendar', 'ICS', 'View Event →', '', 'Oct 4 to Oct 30', 'Extreme Sports', 'Greg Minnaar - Size Matters', '(map)', 'Google Calendar', 'ICS', 'View Event →', '', 'Sep 3 to Sep 27', 'Athletes', 'Mountaineers', 'Tours', 'Hazel Findlay - The Climb Within', '(map)', 'Google Calendar', 'ICS', 'View Event →', 'Back to Top', '', '', '', '']

p_tags = ['One of the biggest personalities in mountain biking, former World Champion Mountain Bike Trials Rider, Martyn Ashton, was already a legend of the sport before his 2012 ‘Road Bike Party’ video and its sequel propelled him to even greater prominence. Despite a life-changing back-break in 2013, Martyn has continued to explore what’s possible on a bike! In Bike Party, Martyn will take audiences through an entertaining look at his life on bikes', "Paralympic gold medalists Karen Dark MBE and Steve Bate MBE share their journey cycling up Kilimanjaro. Wild Tracks delves into challenge, diversity, and human potential with a diverse team. Experience an evening of film and insight uncovering treasures within life's challenges, turning mess into magic. Explore physical demands and emotional healing through mountains, discovering resilience and human connection first-hand.", 'Big wall free solo climbing continues to be a domain that both climbers and the general public struggle to comprehend fully. In Fine Lines, Pete delves into the intricacies of free solo climbing, leading audiences on a narrative spanning from his initial experiences soloing to his monumental 800m big wall free solo ascent of Kjerag in Norway. Embark on a journey through the evolution and challenges of this remarkable endeavour.', "Discover the untold stories, chaos and legendary adventures of mountain biking icon Hans Rey. With career highlights, behind-the-scenes adventures, and the evolution of the sport, it's a wild ride filled with legendary tales and never-before-seen footage. Because, as they say, an adventure isn't complete until things go wrong!", "In ‘rockstar’ climber Hazel Findlay's new show, she'll walk you through the biggest internal battles she's faced in her career and how she's overcome them. She'll take stories from her most difficult ascents and wild expeditions, such as her recent climbing trip to Greenland with Alex Honnold, to talk about the psychological 'walls within' that we all face, such as imposter syndrome, fear of failure, distraction and motivation", 'Everest: The Untold Story celebrates the 70th anniversary of the first successful summit, Kenton Cool - the 16x summit non-Sherpa world record-holder – has created a new show to take audiences on a fascinating journey through the history of the highs and lows of summit attempts on one of the world’s most magnificent mountains: from its first ‘discovery’ as part of the Great Indian Trigonometric Survey, through to the perceived ‘bucket list adventure’ that it is considered today.', '‘It’s All Mental’ is record-breaking aviator, adventurer and author James Ketchell’s second UK tour. The only person on the planet to have climbed Everest, cycled around the world AND rowed an ocean, will be sharing his mind-set and the mentality needed to achieve difficult, and what sometimes feel like unattainable, goals. Having experienced stratospheric highs around the world, to crushing lows in the oceans, James is well prepared to share his experience and advice. This entertaining evening promises to leave you feeling energised and motivated to set your own goals and start realising your dreams.', "Five years on from Mark Beaumont’s famous ‘Around the World in 80 Days', there is no sign of anyone breaking his circumnavigation World Record. Faster captures the wanderlust to find new disciplines of cycling and new wild places, including those closer to home.", '', 'Leo’s brand new show will follow on from his previous tour (The Spectre Expedition, 2019) bringing audiences up to date with his audacious expeditions, primarily focussing on his more recent ascent Mount Roraima, the high, rain forest-engulfed South American plateau which inspired Arthur Conan Doyle’s The Lost World!', '', 'POSTPONED', 'It is with great regret, and reluctance, we are postponing Adrian’s tour due to unforeseen circumstances beyond our control. We very much appreciate, and are very sorry for, any inconvenience or disappointment this may cause – postponing a tour is not something we take lightly! We thank you for your initial ticket purchase and support and we do hope the rescheduled dates, whilst some way off, are still suitable.Venues will, in due course, be in touch with all ticket buyers for this tour directly, to provide options of refunds, credits and/or transferal of tickets.', 'Record-breaking adventurer and author Adrian Hayes takes audiences on a journey through the jungles, seas, deserts, ice caps and mountains of the world that he has devoted much of his life to exploring.', '', 'In this exciting new tour Stephen Venables will recount stories of his adventures; from new Himalayan peaks, arctic dog-sledging, film-making, desert journeys and fifteen sailing voyages, to the snowy mountains of Antarctica. Sharing the fun, excitement, beauty – and the personal tragedies – that make his life a continuing adventure.', 'Follow Pete Whittaker’s journey, from the sub-culture of underground crack climbing, onto the side of the world’s highest big-walls. The story takes you from astronomical lactate pumping athletic feats, to speed solos of the world’s biggest cliffs. Driven by the challenge and the suffering, Pete looks to find that mythical point between the possible and impossible, by climbing not just one, but multiple big walls alone in under 24 hours', 'Only Hull’s second best climber, comedian Andy Kirkpatrick, could take you on a journey from minus fifty degrees to plus fifty, from gun battles in Nairobi, deportation, battles with baboons, elephants and bears, to mundane things like climbing big walls and bigger mountains', 'Kenton Cool holds the British record for Everest ascents, at 14 times. He is the only person in the world to have summited Everest, Lhotse and Nuptse in one season, completing the task in just six days. Undoubtedly, he is one of the world’s most successful and revered climbers. In Everest the Cool Way, Kenton talks about his life of climbing and adventure, from the current state of Everest, climbing Aconcagua and skiing Denali, to the jungles of Bolivia and the mountains of Papua', 'Join Pete from the sub culture of underground crack climbing and onto the side of the world’s highest big walls. The journey takes you from astronomical lactate pumping athletic feats, to speed solos of the world’s biggest cliffs. Driven by the challenge and the suffering, Pete looks to find that mythical point between the possible and impossible, by climbing not just one, but multiple big walls alone in under 24-hours', 'This UK stage tour provides a fascinating insight into Mark Beaumont’s cycling career, having smashed the circumnavigation cycling World Record twice in his career, he now holds this 18,000 mile title in a time of 78 days and 14 hours, averaging 240 miles a day.', 'Sasha will tell her favourite climbing stories and present her film of the history-making ascent of The Trilogy, where she became the first female, and only the second person, to climb the Rocky Mountain triple big walls in a single season. Sasha’s talk and film is sure to inspire climbers and outdoor enthusiasts alike.', 'Sir Chris Bonington was the first mountaineer on the lecture circuit and, this autumn, he will present his “Life & Times” in an audio visual account, covering his sixty years spent in the mountains. With original images and raw footage, this is a rare opportunity to hear about some of the greatest expeditions of the twentieth century.', 'James Ketchell will tour UK theatres, in November 2019, delivering his tales of adventure, endeavour and determination, in an evening experience that will undoubtedly leave young and old feeling motivated and inspired with life lessons learned by the adventurer himself!', 'In Size Matters, Greg Minnaar takes audiences on the journey of his incredible enduring racing career and the story of his life, covering everything from the early days of riding enthusiasm to his rise to the very top, the bikes that helped get him there and the teams behind the legendary rider!', 'One of the best young climbers in the world, Hazel Findlay presents a talk about her life and climbs to explore how we can use a sport such as climbing – something that we are passionate about - to put us in hard places that push us beyond what we thought we were capable of; how in this struggle we can discover the way our minds work and how to ‘hack’ them, so that we can enjoy the experiences we want and not be limited by fear', '', '', '© Speakers From The Edge Limited 2021']

a_tags = list(dict.fromkeys(a_tags))

'''h1_tag_list = []
for tag in h1_tags:
    h1_tag_list.append(tag.replace("\n", " "))


p_tag_list = []
for tag in p_tags:
    p_tag_list.append(tag.replace("\n\n", " "))
'''
    
print("a")
for i, tag in enumerate(a_tags):
    print(i, tag)
'''
print("p")
for i, tag in enumerate(p_tags):
    print(i, tag)

print("p")
for i, tag in enumerate(p_tag_list):
    print(i, tag)
'''
'''print("h3")
for i, tag in enumerate(h3_tags):
    print(i, tag)'''

'''print("span")
for i, tag in enumerate(span_tags):
    print(i, tag)'''
    
'''
event_list = [
    {
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": a_tags[10],
        "description": p_tags[0]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[16],
        "description": p_tags[1]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[18],
        "description": p_tags[2]
    },{
        "name": e["name"],
        "url": url,
        "intro": '',
        "title": '',
        "subtitle": h1_tags[20],
        "description": p_tags[3]
    }
]

#print(centre_details)
for line in event_list:
    for key, value in line.items():
        print(key, ":", value)
'''
