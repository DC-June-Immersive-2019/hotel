hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
   '102': [],
   '103': []
 },
 '2': {
   '201': ['Jack Torrance', 'Wendy Torrance'],
   '202': [],
   '239': []
 },
 '3': {
   '301': ['Neo', 'Trinity', 'Morpheus'],
   '302': [],
   '303': []
 }
}

def check_in():
    floor_num = input("What floor number? ")
    guest_floor_selection = hotel.get(floor_num)
    guest_list = []
    if guest_floor_selection == None:
        print("Not a valid floor number, please select a valid floor")
        check_in()
    room_num = input("What room number? ")
    if hotel.get(floor_num).get(room_num) == None:
        print("Not a valid room selection")
        check_in()
    elif hotel.get(floor_num).get(room_num) != []:
        print("Sorry that room is occupied")
        check_in()
    else:
        num_guests = int(input("How many occupants? "))
        guest_list.append(input("What is your name? " ))
        for num in range(0,num_guests - 1):
            next_guest = input("Please type the name of your next guest: ")
            guest_list.append(next_guest)
        hotel[floor_num][room_num] = guest_list
        print(f"Thanks {guest_list[0]}, enjoy your stay")
        

    #print(hotel)

def check_out():
    floor_num = input("What floor number? ")
    room_num = input("What room number? ")
    if hotel.get(floor_num).get(room_num) == []:
        room_num= input("Sorry, that room is un-occupied. Select a new room: ")
    else:
        hotel[floor_num][room_num] = []
        print("Thanks for staying with us!")

    # print(hotel)

def guest_list():
    p = []
    for j, k in hotel.items():
        for l,m in k.items():
            if len(m) != 0:
                for k in m:
                    p.append(k)
    print(",".join(p))

def checkin_menu():
    while True:
        menu = (input('''Please choose from the following
        Enter '1' for checkin
        Enter '2' for check out
        Enter '3' for Guest List
        Enter '4' to Exit
        '''))
        if menu == '1':
            check_in()
        elif menu == '2':
            check_out()
        elif menu == '3':
            guest_list()
        elif menu == '4':
            break
        else:
            print("Invalid input")

checkin_menu()


#Add menu with 4 options:
# 1 = check in
# 2 = check out
# 3 = list of every guest(names)
# 4 = Exits