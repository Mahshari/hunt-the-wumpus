import random

print("HUNT THE WUMPUS")
instructions = input("Instructions (Y-N) ").strip().upper()
if instructions == "Y":
    print("Welcome to 'Hunt the Wumpus', the wumpus lives in a cave of 20 rooms. each room has 3 tunnels leading to other rooms.  ")
if instructions == "Y":
    print("Hazards: Bottomless pits - two rooms have botomless pits in them, if you go there, you fall into the pit and lose, super bats - two other rooms have super bats. if you go there a bat grabs you and takes you to some other room at random.")
if instructions == "Y":
    print("Wumpus: The wumpus is not bothered by hazards (he has sucker feet and is too big for a bat to lift). Usually he is asleep and is asleep. Two things wake him up: You shooting an arrow or you entering his room. If the wumpus wakes up he moves (P=.75) one room or stays still (P=.25). After that, if he is where you are, he eats you up and you lose!")
if instructions == "Y":
    print("You: each turn you may move or shoot a crooked arrow Moving: You can move one arrow(thru one tunnel) arrows: you can have 5 arrows. you lose when you run out, each arrow can go from 1 to 5 rooms. You aim by telling the computer the rooms you want the arrows to go to. If the arrow cant go that way (if no tunnel) it moves at random to the next room. if the arrow hits the wumpus, you win, if the arrow hits you, you lose.")
else:
    print("You chose not to view the instructions")

# Generate a random room number between 1 and 20
class room:
    def __init__ (self):
        self.number = random.randint(1, 20)

class tunnel:
    # attributes
    def __init__(self):
        self.room_number = random.randint(1,20)

# create room and tunnel instances 
current_room = room()
tunnel_1 = tunnel()
tunnel_2 = tunnel()
tunnel_3 = tunnel()
current_room_2 = room()
current_room_3 = room()
current_room_4 = room()
current_room_5 = room()
current_room_6 = room()
current_room_7 = room()
current_room_8 = room()
current_room_9 = room()
current_room_10 = room()
current_room_11 = room()
current_room_12 = room()
current_room_13 = room()
current_room_14 = room()
current_room_15 = room()
current_room_16 = room()
current_room_17 = room()
current_room_18 = room()
current_room_19 = room()
current_room_20 = room()
current_room_25 = room()
tunnel_4 = tunnel()
tunnel_5 = tunnel()
tunnel_6 = tunnel()
tunnel_7 = tunnel()
tunnel_8 = tunnel()
tunnel_9 = tunnel()
tunnel_10 = tunnel()
tunnel_11 = tunnel()
tunnel_12 = tunnel()
tunnel_13 = tunnel()
tunnel_14 = tunnel()
tunnel_15 = tunnel()
tunnel_16 = tunnel()
tunnel_17 = tunnel()
tunnel_18 = tunnel()
tunnel_19 = tunnel()
tunnel_20 = tunnel()
tunnel_21 = tunnel()
tunnel_22 = tunnel()
tunnel_23 = tunnel()
tunnel_24 = tunnel()
tunnel_25 = tunnel()
tunnel_26 = tunnel()
tunnel_27 = tunnel()
tunnel_28 = tunnel()
tunnel_29 = tunnel()
tunnel_30 = tunnel()
tunnel_31 = tunnel()
tunnel_32 = tunnel()
tunnel_33 = tunnel()
tunnel_34 = tunnel()
tunnel_35 = tunnel()
tunnel_36 = tunnel()
tunnel_37 = tunnel()
tunnel_38 = tunnel()
tunnel_39 = tunnel()
tunnel_40 = tunnel()
tunnel_41 = tunnel()
tunnel_42 = tunnel()
tunnel_43 = tunnel()
tunnel_44 = tunnel()
tunnel_45 = tunnel()
tunnel_46 = tunnel()
tunnel_47 = tunnel()
tunnel_48 = tunnel()
tunnel_49 = tunnel()
tunnel_50 = tunnel()
tunnel_51 = tunnel()
tunnels_52 = tunnel()
tunnels_53 = tunnel()
tunnel_54 = tunnel()
tunnel_55 = tunnel()
tunnel_56 = tunnel()
tunnel_57 = tunnel()
print("Hunt the wumpus")
current_room = print(f"You are in room {current_room.number}")
tunnels = print(f"Tunnels lead to {tunnel_1.room_number} {tunnel_2.room_number} {tunnel_3.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")
    if room1 == (f"{tunnel_1.room_number}"):
        print("AHA You got the wumpus, hee hee hee the wumpus'll get you next time")
input("press enter ") # waits for the user to press enter
print("?")

# Display the current room and tunnels leading to the other rooms
print("HUNT THE WUMPUS")
instructions = input("Instructions (Y-N) ").strip().upper()
if instructions == "Y":
    print("Welcome to 'Hunt the Wumpus', the wumpus lives in a cave of 20 rooms. each room has 3 tunnels leading to other rooms.  ")
if instructions == "Y":
    print("Hazards: Bottomless pits - two rooms have botomless pits in them, if you go there, you fall into the put and lose, super bats - two other rooms have super bats. if you go there a bat grabs you and takes you to some other room at random.")
if instructions == "Y":
    print("Wumpus: The wumpus is not bothered by hazards (he has sucker feet and is too big for a bat to lift). Usually he is asleep and is asleep. Two things wake him up: You shooting an arrow or you entering his room. If the wumpus wakes up he moves (P=.75) one room or stays still (P=.25). After that, if he is where you are, he eats you up and you lose!")
if instructions == "Y":
    print("You: each turn you may move or shoot a crooked arrow Moving: You can move one arrow(thru one tunnel) arrows: you can have 5 arrows. you lose when you run out, each arrow can go from 1 to 5 rooms. You aim by telling the computer the rooms you want the arrows to go to. If the arrow cant go that way (if no tunnel) it moves at random to the next room. if the arrow hits the wumpus, you win, if the arrow hits you, you lose.")
current_room_2 = print(f"You are in room {current_room_2.number}")
tunnels = print(f"Tunnels lead to {tunnel_4.room_number} {tunnel_5.room_number} {tunnel_6.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("room: ")
    if no_of_rooms  == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    if no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    if no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

if shoot_move == ("shoot"):
    print("missed")
    print("4 arrows left")
    print("missed")
    print("3 arrows left")

if shoot_move == ("s"):
    print("missed")
    print("4 arrows left")
    print("missed")
    print("3 arrows left")
print("Hunt the wumpus")
current_room_3 = print(f"You are in room {current_room_3.number}")
tunnels = print(f"Tunnels lead to {tunnel_4.room_number} {tunnel_5.room_number} {tunnel_6.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
if shoot_move == ("shoot"):
    if no_of_rooms == 1: 
        room1 = input("room: ")
if shoot_move == ("shoot"):
    if no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
if shoot_move == ("shoot"):
    if no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
if shoot_move == ("shoot"):
    if no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
if shoot_move == ("shoot"):
    if no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

current_room_4 = print(f"you are in room {current_room_4.number}")
tunnels = print(f"tunnels lead to {tunnel_7.room_number} {tunnel_8.room_number} {tunnel_9.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
elif shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms >= 1: 
        room1 = input("room: ")
    elif no_of_rooms >= 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms >= 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    elif no_of_rooms >= 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")
    if no_of_rooms >= 2 and room2 == '4':
        print("Ouch arrow got you! ha ha ha you lose")
input("press enter ") # waits for the user to press enter
print("?")

print("Hunt the wumpus")
instructions = input("Instructions (Y-N) ").strip().upper()
if instructions == "Y":
    print("Welcome to 'Hunt the Wumpus', the wumpus lives in a cave of 20 rooms. each room has 3 tunnels leading to other rooms.  ")
if instructions == "Y":
    print("Hazards: Bottomless pits - two rooms have botomless pits in them, if you go there, you fall into the put and lose, super bats - two other rooms have super bats. if you go there a bat grabs you and takes you to some other room at random.")
if instructions == "Y":
    print("Wumpus: The wumpus is not bothered by hazards (he has sucker feet and is too big for a bat to lift). Usually he is asleep and is asleep. Two things wake him up: You shooting an arrow or you entering his room. If the wumpus wakes up he moves (P=.75) one room or stays still (P=.25). After that, if he is where you are, he eats you up and you lose!")
if instructions == "Y":
    print("You: each turn you may move or shoot a crooked arrow Moving: You can move one arrow(thru one tunnel) arrows: you can have 5 arrows. you lose when you run out, each arrow can go from 1 to 5 rooms. You aim by telling the computer the rooms you want the arrows to go to. If the arrow cant go that way (if no tunnel) it moves at random to the next room. if the arrow hits the wumpus, you win, if the arrow hits you, you lose.")

print(f"you are in room {current_room_5.number}")
print(f"tunnels lead to {tunnel_11.room_number} {tunnel_12.room_number} {tunnel_13.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")
    if no_of_rooms == 1 and room1 == str(tunnel_13.room_number):
        print("AHA YOU GOT THE WUMPUS")
        print("HEE HEE HEE - THE WUMPUS'LL GET YOU NEXT TIME")
input("press enter ") # waits for the user to press enter
print("?")
print("hunt the wumpus")
instructions = input("Instructions (Y-N) ").strip().upper()
if instructions == "Y":
    print("Welcome to 'Hunt the Wumpus', the wumpus lives in a cave of 20 rooms. each room has 3 tunnels leading to other rooms.  ")
if instructions == "Y":
    print("Hazards: Bottomless pits - two rooms have botomless pits in them, if you go there, you fall into the put and lose, super bats - two other rooms have super bats. if you go there a bat grabs you and takes you to some other room at random.")
if instructions == "Y":
    print("Wumpus: The wumpus is not bothered by hazards (he has sucker feet and is too big for a bat to lift). Usually he is asleep and is asleep. Two things wake him up: You shooting an arrow or you entering his room. If the wumpus wakes up he moves (P=.75) one room or stays still (P=.25). After that, if he is where you are, he eats you up and you lose!")
if instructions == "Y":
    print("You: each turn you may move or shoot a crooked arrow Moving: You can move one arrow(thru one tunnel) arrows: you can have 5 arrows. you lose when you run out, each arrow can go from 1 to 5 rooms. You aim by telling the computer the rooms you want the arrows to go to. If the arrow cant go that way (if no tunnel) it moves at random to the next room. if the arrow hits the wumpus, you win, if the arrow hits you, you lose.")

print(f"You are in room {current_room_6.number}")
print(f"tunnels lead to {tunnel_14.room_number} {tunnel_15.room_number} {tunnel_16.room_number}")
shoot_move = input("shoot or move ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ") 
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

print(f"You are in Room {current_room_7.number}")
print(f"tunnels lead to {tunnel_19.room_number} {tunnel_20.room_number} {tunnel_21.room_number}")
shoot_move = input("S-M ")
if shoot_move == ("move"):
    move_to = input("where to ")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ") 
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

print(f"you are in Room {current_room_8.number}")
print(f"tunnels lead to {tunnel_22.room_number} {tunnel_23.room_number} {tunnel_24.room_number}")
shoot_move = input("S-M" )
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
    print("bats nearby")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ") 
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

print(f"you are in Room {current_room_9.number}")
print(f"tunnels lead to {tunnel_25.room_number} {tunnel_26.room_number} {tunnel_27.room_number}")
shoot_move = input("S-M" )
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")

if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ") 
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")
print(f"you are in Room {current_room_10.number}")
print(f"tunnels lead to {tunnel_28.room_number} {tunnel_29.room_number} {tunnel_30.room_number}")
shoot_move = input("S-M" )
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

    if room1 == input(f"{tunnel_30}"):
        print("missed")
        print("4 arrows left")
                
print(f"you are in Room {current_room_11.number}")
print(f"tunnels lead to {tunnel_31.room_number} {tunnel_32.room_number} {tunnel_33.room_number}")
shoot_move = input("S-M" )
shoot_move = input("S-M" )
if shoot_move == ("move"):
    move_to = input("where to ")
if shoot_move == ("shoot"):
    no_of_rooms = input(f"no of rooms (1-5) ")
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    if no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ") 
    if no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    if no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
print(f"you are in Room {current_room_12.number}")
print(f"tunnels lead to {tunnel_34.room_number} {tunnel_34.room_number} {tunnel_36.room_number}")
shoot_move = input("S-M" )
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == ("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if shoot_move == ("shoot"):
        if no_of_rooms == 1: 
            room1 = input("room:")
    if shoot_move == ("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == ("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == ("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == ("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if room1 == input(f"{tunnel_30}"):
        print("missed")
        print("4 arrows left")            
    elif no_of_rooms == 2:
        room1 = input("room: ")
        room2 = input("Room: ")
    elif no_of_rooms == 3:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
    elif no_of_rooms == 4:
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
    elif no_of_rooms == 5: 
        room1 = input("room: ")
        room2 = input("room: ")
        room3 = input("room: ")
        room4 = input("room: ")
        room5 = input("Room: ")

if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")

print(f"You are in Room {current_room_12.number}")
tunnels = f"Tunnels lead to {tunnel_37.room_number}, {tunnel_38.room_number}, {tunnel_39.room_number}"
print(tunnels)

shoot_move = input("Shoot or Move? (S-M): ").strip().lower()
if shoot_move == "move":
    move_to = input("Where to? ").strip()
    if move_to == str(tunnel_38.room_number):  # Compare with the actual room number
        print("Zap--superbatsnatch! Elsewhereville for you")
    else:
        print(f"You moved to Room {move_to}")

if shoot_move == input("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")

print(f"you are in room {current_room_13.number}")
tunnels = (f"tunnels lead to {tunnel_40.room_number} {tunnel_41.room_number} {tunnel_42.room_number}")
shoot_move = input("S-M")
if shoot_move == input("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
if shoot_move == input("shoot"):
    rooms = input(f"no of rooms ")
    print("missed")
    print("3 arrows left")

print(f"you are in {current_room_14.number}")
tunnels = (f"tunnels lead to {tunnel_43.room_number} {tunnel_44.room_number} {tunnel_45.room_number} ")
shoot_move = input("S-M")
if shoot_move == ("move"):
    move_to = input("where to ")
    print(f"you are in room {move_to}")
if shoot_move == input("shoot"):
    no_of_rooms = input("no of rooms ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 1: 
            room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
print(f"you are in {current_room_15.number}")
tunnels = (f"tunnels lead to {tunnel_46.room_number} {tunnel_47.room_number} {tunnel_48.room_number} ")
shoot_move = input("S-M")
if shoot_move == ("move"): 
    move_to = input("where to")
if shoot_move == input("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if shoot_move == input("shoot"):
        if no_of_rooms == 1: 
            room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
tunnels = (f"tunnels lead to {tunnel_49.room_number} {tunnel_50.room_number} {tunnel_51.room_number}")
shoot_move = input("S-M ")
if shoot_move == ("move"):
    move_to = input("Where to")
    if move_to == input(f"Where to {tunnel_50}"):
        print("I feel a draft!")
if shoot_move == input("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if no_of_rooms == 1: 
        room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
tunnels = (f"tunnels lead to {tunnels_52.room_number} {tunnels_53.room_number} {tunnel_54.room_number}")
shoot_move = input("S-M ")
if shoot_move == input("shoot"):
    rooms = input(f"no of rooms ")
    print("missed")
    print("2 arrows left")
    print("I feel a draft")
print(f"you are in {current_room_16.number}")
tunnels = (f"tunnels lead to {tunnel_55.room_number} {tunnel_56.room_number} {tunnel_57.room_number}")
shoot_move = input("S-M")
if shoot_move == ("move"):
    move_to = input("where to")
    if move_to == input(f"{tunnel_56}"):
        print("oops burned a wumpus ")
        print("tsk tsk tsk wumpus got you")
        print("ha ha ha you lose")
if shoot_move == input("shoot"):
    no_of_rooms = int(input("no of rooms "))
    if shoot_move == input("shoot"):
        if no_of_rooms == 1: 
            room1 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 2:
            room1 = input("room: ")
            room2 = input("Room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 3:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 4:
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
    if shoot_move == input("shoot"):
        if no_of_rooms == 5: 
            room1 = input("room: ")
            room2 = input("room: ")
            room3 = input("room: ")
            room4 = input("room: ")
            room5 = input("Room: ")
input("press enter ") # waits for the user to press enter
print("?")


