import re

p_tags = ['Our open plan centre is a great social space to climb with friends! It features our unique top-out boulder, comp room, overhanging, slab and vertical walls, all set with our state of the art climbing hold selection from the best manufacturers around.', 'The large dedicated kids and beginners area is available for you to learn or bring your kids down before progressing to the main centre.', 'Need to hire some equipment for your session? we offer climbing shoe hire in a huge range of sizes, chalk bag hire and a shop selling all the bits you need and merchandise.', 'There is ample free on-site parking, and a large bike storage. our location is just a 15 min walk from Burley Park train station and 30 min walk from Leeds central train station.', 'The doors open at 6am every weekday morning and there are plush changing rooms with showers, lockers, and toilets so you can get ready for your day after an early climb. grab a free filter coffee before 9am to power up your climb!', 'Waiver', 'We have different prices to suit your pocket : Pay per Visit, Monthly Memberships, Annual Memberships & 10 Climb Passes.', 'Prices', 'Once you have completed your Adult Intro session, you can climb independently in the centre. When you feel confident you may also supervise 2 guests per visit; it’s a great way to introduce your friends and family to bouldering', 'Units 12, 14 & 15', 'Kirkstall Industrial Park', 'Leeds', 'LS4 2AZ', 'info@climbinglab.co.uk', 'Tel: 01132632742', 'Monday to Friday: 6:00am - 10pm ', 'Saturday/Sunday: 10am - 9pm', '© Copyright  2023   The Climbing Lab  ']

'''for i, tag in enumerate(p_tags):
    print(i, tag)'''


p_tags_phone = re.sub(r'[([T][e][l](: )', r'', p_tags[14])
print(p_tags_phone)
print(type(p_tags_phone))

centre_details = [
    {
        "street": p_tags[9],
        "street_area": p_tags[10],
        "city": p_tags[11],
        "postcode": p_tags[12],
        "email": p_tags[13],
        "phone": p_tags_phone
    }
]

print(centre_details)
