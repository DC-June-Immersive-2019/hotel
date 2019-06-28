# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
 },
 '2': {
   '237': ['Jack Torrance', 'Wendy Torrance'],
 },
 '3': {
   '333': ['Neo', 'Trinity', 'Morpheus']
 }
}

inNout = input("Hi there! Are you checking in or out? ")
# floor1 = hotel['1']['101']
# floor2 = hotel['2']['237']
# floor3 = hotel['3']['333']

if inNout == "in":
    floor = int(input("What floor? "))
    room = int(input("Room number? "))
    if floor == 1 and room == 101:
        occupants = int(input("How many occupants? "))
        if occupants == 2:
            print("Okay, " + str(hotel['1']['101']) + " you are both checked in!")
    if floor == 2 and room == 237:
        occupants = int(input("How many occupants? "))
        if occupants == 2:
            print("Okay, " + str(hotel['2']['237']) + " you are both checked in!")
    if floor == 3 and room == 333:
        occupants = int(input("How many occupants? "))
        if occupants == 3:
            print("Okay, " + str(hotel['3']['333']) + " you guys are checked in!")
else:
    floor = input("What floor? ")
    room = input("What room? ")
    ppl = ""
    for name in hotel[floor][room]:
        ppl = ppl + name + ", "
    print("Okay, " + ppl + " you are checked out.")
    del hotel[floor][room]
  









    # if ans == 1 and ans2 == 101:
    #     print("Okay, " + str(hotel['1']['101']) + " you are both checked out.")
    # if ans == 2 and ans2 == 237:
    #     print("Okay, " + str(hotel['2']['237']) + " you are both checked out.")
    # if ans == 3 and ans2 == 333:
    #     print("Okay, " + str(hotel['3']['333']) + " you are all checked out.")
    


        

