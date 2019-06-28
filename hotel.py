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
#print(hotel["1"]["101"][1])

## Display a menu asking whether to check in or check out.
## Prompt the user for a floor number, then a room number.
## If checking in, ask for the number of occupants and what their names are.
## If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
## Do not allow checking out of a room that isn't occupied.


#inputguestfloor = input("What floor are you on? >> ")
#inputguestroom = input("what is your room number? >> ")
#multiguest = True


#prompt
inputcheckinout = input("Do you want to check IN or Out? >> ")
#checkin
if inputcheckinout.lower() == "in":
    guestname = input("what is your name? >> ")
    numbguest = input("how many people are in your party? >> ")
    if int(numbguest) > 1:  
        input("what are the names in your party? >>")
#checkout 
else: 
    inputguestfloor = input("What floor are you on? >> ")
    inputguestroom = input("what is your room number? >> ")
    if hotel.get(inputguestfloor) and hotel.get(inputguestfloor).get(inputguestroom) != None:
        del hotel[inputguestfloor][inputguestroom]
    else:
        print("that is an empty room")



print(hotel)
