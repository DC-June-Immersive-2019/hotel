# File: hotel_manager_app.py

""" This is a program that allows a user to manage a hotel given
the number of floors and number of rooms per floor. """

##### Initialize the specs for the hotel in question

hotel_total_floors = 5 # Set in the range 1-9
hotel_rooms_per_floor = 99 # Set in the range 1-99
hotel_name = "The Murder Hotel"

hotel = {str(floor_num) : {(str(floor_num) + str(room_num).zfill(2)) : [] for room_num in range(1, hotel_rooms_per_floor + 1)} for floor_num in range(1, hotel_total_floors + 1)}

# Provide some nonsense data so that some rooms are already occupied

hotel["1"]["101"] = ["George Jefferson", "Wheezy Jefferson"]
hotel["2"]["237"] = ["Jack Torrance", "Wendy Torrance"]
hotel["3"]["333"] = ["Neo", "Trinity", "Morpheus"]

##### Ensure that the floor and room numbers desired by the hotel guest are valid

def floor_and_room_num():
  floor_num = int(input("\nWhat floor number? "))
  while floor_num not in range(1, hotel_total_floors + 1):
    floor_num = int(input("Only 1-" + str(hotel_total_floors) + " are valid floor numbers. Please enter a valid floor number: "))
  room_num = int(input("What room number? "))
  while room_num not in range(floor_num * 100 + 1, floor_num * 100 + hotel_rooms_per_floor + 1):
    room_num = int(input("Only " + str(floor_num * 100 + 1) + "-" + str(floor_num * 100 + hotel_rooms_per_floor) + " are valid room numbers. Please enter a valid room number: "))
  return str(floor_num), str(room_num)

##### Check the guest in and update the hotel based on the new occupants

def check_in(floor, room):
  while hotel[floor][room] != []:
    original_room = room
    room = input("The room you are trying to check into is already occupied. Sorry for the inconvenience! Please enter another room number to check into: ")
    if hotel[floor].get(room) is None:
      print("This room does not exist on the floor you desire. Please enter a valid room number.")
      room = original_room
  new_occupants_num = int(input("Enter the number of occupants checking in: "))
  new_occupants = []
  for i in range(1, new_occupants_num + 1):
    occupant = input("Enter the first and last name (no commas) of occupant " + str(i) + ": ")
    new_occupants.append(occupant)
  hotel[floor][room] = new_occupants

##### Check out the guests and clear their room of their names

def check_out(floor, room):
  while hotel[floor].get(room) is None or hotel[floor][room] == []:
    room = input("There is currently no one checked into this room. Please enter another room to check out of: ")
  hotel[floor][room].clear()

##### The Hotel Manager App

def main():
  run_hotel_manager = ""
  while run_hotel_manager == "":

    # Determine if guest is planning to check in or out

    response = input("Hello! Thank you for staying at " + hotel_name + ". Will you be checking in or out today (I / O)? ")
    valid_check_in_responses = ["i", "I", "in", "In"]
    valid_check_out_responses = ["o", "O", "out", "Out"]
    while response not in valid_check_in_responses and response not in valid_check_out_responses:
      response = input("Please enter a valid option (I / O): ")

    # Ensure that the floor and room numbers provided by the guest are valid options for check in or check out

    floor_num, room_num = floor_and_room_num()

    # Check the guest in or out depeneding on their response

    if response in valid_check_in_responses:
      check_in(floor_num, room_num)
      print("\nYou have successfully checked into room " + room_num + " on floor " + floor_num + ".")
      print("\nEnjoy your stay!")
      print()
    else:
      check_out(floor_num, room_num)
      print("\nYou have successfully checked out of room " + room_num + " on floor " + floor_num + ".")
      print("\nThank you for visiting " + hotel_name + ", and be sure to come again soon!")
      print()
    
    # Prompt the guest to restart the check in/out process for the next guess or close the program

    run_hotel_manager = input("Press <Enter> to restart the check in/out process or any letter to close. ")
  
  # Print a copy of the hotel to see its current status

  print(hotel)

main()