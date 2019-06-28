

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
stop = True
while stop:
    check_inBoolean = False

    while check_inBoolean == False:
        Userinput1 = (input("Would you like to check in or check out? ")).lower()
        if Userinput1 == "check in" or Userinput1 == "check out":
            check_inBoolean = True
        else:
            print("invalid input")
        




    roomboolean1 =  False
    roomboolean2 =  False
    roomboolean = False
    roomNumber1 = ""
    while roomboolean == False:
        roomNumber = input("What is your floor number? (must be from 1- 599)")
        
        roomNumber1 = roomNumber[1:]
        roomint = int(roomNumber1)

        floorNumber =  roomNumber[:1]
        floorint = int(floorNumber)

        if 0<= roomint < 100 or 0< floorint < 6:
            roomboolean =  True
        else: 
            roomboolean = False
        




    if Userinput1 == "check in":
        
        if hotel[floorNumber].get(roomNumber) == None:
            occupants = int(input("How many people are checking in? "))
            occupants_check = 0
            occupant_list = []
            while occupants_check < occupants:
                occupant_text = str(occupants_check +1)
                occupant_name = input("What is the occupant "+ occupant_text+" name? ")
                occupant_list.append(occupant_name)
                
                hotel[floorNumber][roomNumber] = occupant_list
                occupants_check += 1 
        else:
            print("Sorry that room is taken.")
    else:
        if hotel[floorNumber].get(roomNumber):
            del hotel[floorNumber][roomNumber]   
        else:
            print("That room is empty")
    print(hotel)

    end_boolean = True
    while end_boolean:
            Userinput5 = (input("Wanna do another check in or check out? (Y or N) ")).lower()
            if Userinput5 == "y":
                end_boolean = False
            elif Userinput5 == "n":
                end_boolean = True
            else:
                print("invalid input")
print("GoodBye")

