hotel = {
 '1': {
   '101': [],
   '102': [],
   '103': [],
 },
 '2': {
   '201': [],
   '202': [],
   '203': [],
 },
 '3': {
   '301': [],
   '302': [],
   '303': [],
 }
}

def checkin() :
    floor = input("What Floor? ")
    if int(floor) in range(1,4) :
        room = input("What Room? ")
        if int(room) in range((int(floor)*100+1),(int(floor)*100+4)) :
            if not hotel[floor][room] :
                occupants = int(input("How many occupants? "))
                names = []
                for x in range(0, occupants) :
                    names.append(input("Enter occupant name: ")) 
                hotel[floor] = {room:names}
            else :
                print("That room is occupied!" )
        else :
                print("Invalid Room!" )
    else :
        print("That floor doesn't exist!")
    
    
def checkout() :
    floor = input("What Floor? ")
    if int(floor) in range(1,4) :
        room = input("What Room? ")
        if int(room) in range((int(floor)*100+1),(int(floor)*100+4)) :
            if hotel[floor][room] :
                del hotel[floor][room]
            else:
                print("That room is unoccupied!" )
        else :
            print("Invalid Room!" )
    else :
        print("That floor doesn't exist!")

while True :
    answer = input("Check in, check out, or exit? (In/Out/Exit) ")
    if answer.lower() == "in" :
        checkin()
        print(hotel)
    elif answer.lower() == "out":
        checkout()
        print(hotel)
    elif answer.lower() == "exit":
        break
    else:
        print("Invalid Input! ")

    