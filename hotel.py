"""
Hotel Management App
Instructions
Let's imagine that you're running a hotel, and you want to keep track of guests by floor and room number:

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
Write a program that works with this hotel data:

Display a menu asking whether to check in or check out.
Prompt the user for a floor number, then a room number.
If checking in, ask for the number of occupants and what their names are.
If checking out, remove the occupants from that room.
Do not allow anyone to check into a room that is already occupied.
Do not allow checking out of a room that isn't occupied.
"""


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



def checked_in_status():
    checked = False
    while not checked:
        checked_in_out = input("1. Check in \n2. Check out: ")
        if checked_in_out.lower() == "check in" or checked_in_out.lower() == "in" or checked_in_out.lower() == "i" or checked_in_out == "1":
            return True
            checked = True
        elif checked_in_out.lower() == "check out" or checked_in_out.lower() == "out" or checked_in_out.lower() == "o" or checked_in_out == "2":
            return False
            checked = True
        else:
            print("Not an option")
    
def check_in():
    status = True
    while status:
        check = checked_in_status()
        floor_num = 0
        room_num = 0
        while floor_num not in ["1","2","3"]:
            floor_num = input("What floor number (1-3)?: ")
            if floor_num not in ["1","2","3"]:
                print("That isn't a floor to this building.")
        while not (int(room_num) > 0 and int(room_num) < 400):
            room_num = input("What room number?: ")
            if not (int(room_num) > 0 and int(room_num) < 400):
                print("That isn't a room to this building.")                
        # num_occupants = input("Number of occupants?: ")
        if check == True:
            if hotel.get(floor_num).get(room_num) != None:
                print("Already has occupants")
            else:
                # name_occupants = input("List of occupant names? (as a list): ")
                # hotel[floor_num][room_num] = name_occupants
                name_occupants2 = []
                for i in range(int(input("How many occupants?: "))):
                  name_occupants2.append(input("Name of occupant %s: " % str(i+1)))
                hotel[floor_num][room_num] = name_occupants2
                print("You're now checked in.")
        else:
            if hotel.get(floor_num).get(room_num) == None:
                print("Nobody is checked in there")        
            else:
                del hotel[floor_num][room_num]
                print("You're now checked out.")
        ask = input("Do you want to do anything else? Y or N? ")
        if ask.lower() == "n":
            print("Goodbye.")
            status = False
        elif ask.lower() != "y":
            print ("That's not an option.  Goodbye.")
            status = False
        else:
            print("What else can I help you with?")

check_in()
print(hotel)