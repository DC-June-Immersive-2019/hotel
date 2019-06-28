#####Assignment Parameters#####
## Display a menu asking whether to check in or check out.
## Prompt the user for a floor number, then a room number.
## If checking in, ask for the number of occupants and what their names are.
## If checking out, remove the occupants from that room.
## not allow anyone to check into a room that is already occupied.
## Do not allow checking out of a room that isn't occupied.

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

symbol = "*"
#wide = int(input('how wide do you want? ..'))
#tall = int(input('how tall do you want? ..'))
#userinput = input("what do you want your banner to say?")
lengbanner = "Awesome-o Hotel Management Software"#len(userinput)
print(symbol*(len(lengbanner)+2))
for xx in range (1):
    print(symbol+(lengbanner)+symbol)
print(symbol*(len(lengbanner)+2))




def checkincheck():
    numbguest = input("how many people are in your party? >> ")
    if int(numbguest) > 1:  
        names = input("""please provide your name and a list of your guests. (separated by commas) 
    >>""")
    else:
        input("what is your name?")    
    inputcheckinfloor = input("what floor do you want? >> ")
    inputcheckinroom = input("what room do you want? >> ")
    if hotel.get(inputcheckinfloor) and hotel.get(inputcheckinfloor).get(inputcheckinroom) == None:
        print("ok, here you go.")
        hotel[inputcheckinfloor][inputcheckinroom] = [names]
        print(hotel)
    else: 
        print('Sorry that room is occupied.')

def checkout():
    inputguestfloor = input("What floor are you on? >> ")
    inputguestroom = input("what is your room number? >> ")
    if hotel.get(inputguestfloor) and hotel.get(inputguestfloor).get(inputguestroom) != None:
        del hotel[inputguestfloor][inputguestroom]
        print(hotel)
    else:
        print("That is an empty room.")

def prompt():
    contin = True
    while contin: 
        inputcheckinout = input("""Are you checking-in or checking-out?
Press 1 for Check-In Menu
Press 2 for Check-Out Menu
        >>""")
        if inputcheckinout.lower() == "1":
            checkincheck()
        elif inputcheckinout.lower() == "2":
            checkout()
        else:
            print("I'm sorry, that is an incorrect key.")
        tryagain = input("do you want to start over?")
        if tryagain.lower() == "yes":
            contin = True
        else:
            contin = False

prompt()


