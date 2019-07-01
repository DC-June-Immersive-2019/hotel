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


check = input("Would you like to Check in or Check Out")
floor_num = input("What floor would you like")
room_num = input("Room Number ?")

occupant_counter = 0
name_list = []

# ask number of occupants and their names
if check == 'in':
    occupant_number = input('How many occupants?: ')
    while int(occupant_number) > occupant_counter:
        ask_name = input('Name: ')
        name_list.append(ask_name)
        occupant_counter += 1

# print(name_list)


# check and see if floor number and room is available, and then add new occupants
    for floor in hotel:
        if floor_num in floor:
            if room_num not in hotel[floor]:
                hotel[floor][room_num] = name_list
            else:
                print("Room is already occupied.")
    

# checking out of the hotel
elif check == 'out':
    for floor in hotel:
        if floor_num in floor:
            if room_num in hotel[floor]:
                del hotel[floor][room_num] 
            elif room_num not in hotel[floor]:
                print("That room number don't exist, try again")
        else:
            print("The floor don't exist, try again")
      

print(hotel)

