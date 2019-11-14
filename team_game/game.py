import random
import time
import winsound

from items import *
from map import *
from gameparser import *
from player import *
from maze import *
from graphics import *


def print_maze_exit(direction, leads_to):
    print("<GO " + direction.upper() + ">")


def print_maze_menu(exits):
    print("\n\nYou can:\n")

    for direction in exits:
        print_maze_exit(direction, maze_leads_to(exits, direction))

    for dead_end in maze_dead_ends:
        if dead_end == current_maze_room["name"]:
            print("DEAD END!")

    print("\nEXIT to exit game")

    print("\nWhat do you want to do?")


def maze_leads_to(exits, direction):
    return maze_junctions[exits[direction]]["name"]


def maze_menu(exits):
    # Display menu
    print_maze_menu(exits)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def list_items(items):
    """
    This function returns a comma seperates list of items in the player's or npc's inventory.

    It takes as input the list of items.
    """
    item_list = ""

    # This loop concatanates all the items inputted with a ',' between them
    for item in items:
        item_list = item_list + (str(item["name"]) + ", ")

    # Returns the concatanated list without the final character(',')
    return item_list[:-2]


def add_mass(item_mass):
    """
    This function adds the mass of the item picked up by the player to the player's mass,
    if the mass exceeds the max the player can carry, the player does not pick up the item.

    It takes as input the item.
    """

    # This make the function use the project wide mass variable
    global mass

    # Here the program checks if the player can carry around any more weight(mass)
    if mass + item_mass > 3:
        # If not, the object cannot be added to the player's inventory
        return False
    else:
        # If yes, the object can be added to the player's inventory and it is
        # added to the mass
        mass = mass + item_mass
        return True


def remove_mass(item_mass):
    """
    This funcion does the opposite to the add_mass function, when the player drops an item
    the mass is removed from the player's total mass.

    It takes as input the item.
    """

    # This makes the function use the program wide mass variable
    global mass

    # Whenever the player removes an item from their inventory, it removes its
    # mass as well
    mass = mass - item_mass


def print_room_items(room):
    """
    This function prints a comma seperated list of items present in the current room.

    It takes as input the current room.
    """

    # Checks if the list of items is not empty
    if list_items(room["visible_items"]) != "":
        # Concatanates the start and end of the line with the list of items and
        # a blank line
        print("There is " + str(list_items(room["visible_items"])) + " here.")
        print("")


def print_inventory_items(items):
    """
    This funcion prints a comma seperated list of items present in the player's inventory.

    It takes as input the items in the inventory.
    """

    # It tries for an IndexError
    try:
        # Creates an empty string in case the items[] is empty
        items_in_inv = ""
        if items[0] != "":
            # It creates a list of the items in the player's inventory
            items_in_inv = list_items(items)

            # Then the list is printed
            print("You have " + items_in_inv + ".\n")
    # If there is an IndexError, the funcion does nothing
    except IndexError:
        pass


def print_room(room):
    """
    This function prints the name, description and items of the current room.

    It takes as input the current room.
    """
    # Display room name
    print("\n" + room["name"].upper() + "\n")

    for item in room["visible_items"]:
        if item["id"] == "book":
            winsound.PlaySound("chest.wav", winsound.SND_FILENAME)
            time.sleep(0)
            show_graphic(book)
        elif item["id"] == "key":
            winsound.PlaySound("chest.wav", winsound.SND_FILENAME)
            time.sleep(0)
            show_graphic(key)
        elif item["id"] == "phone":
            winsound.PlaySound("chest.wav", winsound.SND_FILENAME)
            time.sleep(0)
            show_graphic(phone)

    if current_room["name"] == "The Library":
        show_graphic(bookcase)

    # Display room description
    print(room["description"] + "\n")

    # Display room items
    print_room_items(room)


def exit_leads_to(exits, direction):
    """
    This function returns the name of the room where the exit leads to.

    It takes as input the room exits and direction.
    """

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """
    This function prints the direction and name of the room which it leads to.

    It takes as input the direction and the exit it leads to.
    """
    if inventory != []:
        for item in inventory:
            if item["id"] == "candle":
                if item["type"] == "Light" and item["life"] > 0:
                    if rooms[leads_to]["visible"] == True:
                        print("<GO " + direction.upper() + "> to " + leads_to + ".")
                        return
                else:
                    if rooms[leads_to]["visible"] == True:
                        print("<GO " + direction.upper() + ">")
    else:
        if rooms[leads_to]["visible"] == True:
            print("<GO " + direction.upper() + ">")
            return

def print_menu(exits, room_items, inv_items):
    """
    This function prints a menu of options the player has at every turn.

    It takes as input the exits, room items, the items in the player's inventory
    and the present npc's inventory.
    """

    print("\nYou can:\n")

    # Prints the available exits to the player
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    print()

    # Prints the available items to pick up
    for item in room_items:
        if item["enable pickup"] == True:
            print("<TAKE " + item["id"].upper() + "> to take " + item["name"] + ".")

    # Prints the available items to drop
    for item in inv_items:
        print("<DROP " + item["id"].upper() + "> to drop your " + item["name"] + ".")

    for item in inv_items:
        if item["type"] == "Food":
            print("<EAT " + item["id"].upper() + "> to eat the " + item["name"] + ".")

    for item in room_items:
        if item["id"] == "bed":
            print("<REST> to rest in the bed")

    for item in inv_items:
        if item["id"] == "candle" and item["type"] == "NONE":
            for i in inv_items:
                if i["id"] == "matches":
                    print("<LIGHT CANDLE> to light a candle.")

    if current_room["name"] == "The End of the Hallway" and room_living["visible"] == False and current_room["examined"] == True:
        for item in inventory:
            if item["id"] == "key":
                print("<USE KEY ON PAINTING> to try the keyhole.")

    if current_room["name"] == "The Library" and room_secret["visible"] == False and current_room["examined"] == True:
        for item in inventory:
            if item["id"] == "book":
                print("<USE BOOK ON BOOKCASE> to replace the book in the bookshelf.")

    print()

    if current_room["examined"] == False:
        print("<EXAMINE> to examine the room in more detail.\n")

    print("<EXIT> to exit game")

    print("\nWhat do you want to do?")


def valid_exit(exits, chosen_exit):
    """
    This function checks if the desired exit exists, it retunrs True in this case,
    False if this is not the case.

    It takes as input the exits and the user choice.
    """
    return chosen_exit in exits


def go(direction, room):
    """
    This function enable the player to move around the map.

    It takes as input the player choice(direction).
    """

    # This makes the funcion use the program wide variables
    global current_room
    global current_maze_room
    global maze
    global hatch
    global riddle_answered

    jumpscare(direction, room)

    if current_room["name"] == "The End of the Hallway" and direction == "down" and room_living["visible"] == False:
        print("You cannot go there.")
        return

    if current_room["name"] == "The Library" and direction == "east" and room_secret["visible"] == False:
        print("You cannot go there.")
        return

    if current_room["name"] == "The Basement" and riddle_answered == False:
        print("riddle must be answered")
        return

    if current_room["name"] == "The Living Room":
        if hatch != True:
            if move(room["exits"], direction)["name"] == "The Maze":
                print("YOU FALL THROUGH A HOLE IN THE FLOOR")
                current_room = rooms["The Basement"]
                hatch = True
                return
        else:
            print("You now notice the trapdoor in the floor.")

    if valid_exit(room["exits"], direction):
        # If the chosen exit is valid, the current_room is changed to the new room
        if maze != True:
            room = rooms[room["exits"][direction]]
            current_room = room
        else:
            if current_maze_room == maze_junctions["The Maze"] and direction == "west":
                room = rooms["The Living Room"]
                current_room = room
                maze = False
            else:
                room = maze_junctions[room["exits"][direction]]
                current_maze_room = room
    else:
        # If not, the user is alerted to the fact
        print("You cannot go there.")

    if current_room == rooms["The Maze"]:
        maze = True

    if current_maze_room == maze_junctions["The Living Room"]:
        maze = False


def take(item_id):
    """
    This function enables the player to pick up items from the enviroment. It tells
     the player what item they have picked up. If the item is not present, it
    alerts the player.

    It takes as input the player choice(item id).
    """

    # Flag to check if the item has been picked up (default false)
    flag = False
    # Loops through the items in the room
    for item in current_room["visible_items"]:
        # Checks if the user choice is the same as one of the items in the room
        if item["id"] == item_id:
            if item["enable pickup"] == True:
                # Checks if the add_to_mass returns True meaning that the player can
                # carry the item
                if add_mass(item["mass"]):
                    # Adds item to player inventory
                    inventory.append(item)
                    # Removes item from the room
                    current_room["visible_items"].remove(item)
                    # Sets the flag to true, meaning that the item has been picked up
                    flag = True

    if flag:
        # Item picked up
        pass
    else:
        # Item not picked up
        print("You cannot take that.")


def drop(item_id):
    """
    This function enables the player to drop items in the room they are currently
    in. If the player does not have the item, thry are alerted.

    It takes as input the player choice(item id).
    """

    # Flag to check if the item has been dropped (default false)
    flag = False
    # Loops through every item in the player's inventory
    for item in inventory:
        # Checks if the user choice is the same as one of the items in the
        # player's inventory
        if item["id"] == item_id:
            # Removes the item from the player's inventory
            inventory.remove(item)
            # Adds the item to the current_room
            current_room["visible_items"].append(item)
            # Removes the mass from the player
            remove_mass(item["mass"])
            # Sets flag to True, meaning that the item has been dropped
            flag = True

    if flag:
        # Item dropped
        pass
    else:
        # Item not dropped
        print("You cannot drop that.")


def give(item_id, person):
    """
    This function enable the player to give items to the npc's present in the
    room/tile. If the player does not have the item, they are alerted.

    It takes as input the player choice(item id, npc).
    """

    # Flag to check if the item has been given to an npcs (default false)
    flag = False
    # Loops through all items in the player's inventory
    for item in inventory:
        # Checks if the user choice is the same as one of the items in the inventory
        if item["id"] == item_id:
            # Removes item from player's inventory
            inventory.remove(item)
            # Adds item to the npc inventory
            current_room["npcs"][names[person]].append(item)
            # Removes mass from the player
            remove_mass(item["mass"])
            # Sets flag to true, meaning that the item has been given to the npc
            flag = True
            # Alerts the player of action
            print("You have given your " + item["name"] + " to " + names[person] + ".")

    if flag:
        # Item given
        pass
    else:
        # Item not given
        print("You cannot give this item to " + names[person] + ".")


def retrieve(item_id, person):
    """
    This function enables the player to retrieve items from an npc in the room they
    are currently in. If the npc is not present or does not have the item the player
    is alerted.

    It takes as input the player choice(item id, npc)
    """

    # Flag to check if the item has been retrieved from an npc (default flase)
    flag = False
    # Loops through the names of the npc's in the room
    for name in current_room["npcs"]:
        # Loops through the items said npc's inventory
        for item in current_room["npcs"][name]:
            # Checks if the user choice is the same as one in the npc's inventory
            if item["id"] == item_id:
                # Checks if the item can be added to the mass and in turn adds it
                if add_mass(item["mass"]):
                    # Adds item to the player's inventory
                    inventory.append(item)
                    # Removes the item from the npc's inventory
                    current_room["npcs"][name].remove(item)
                    # Sets flag to true, meaning that the player has retrieved
                    # the item from the npc
                    flag = True
                    # Alerts the player of action
                    print("You have retrieved your " + item["name"] + " from " + names[person] + ".")

    if flag:
        # Item retrieved
        pass
    else:
        # Item not retrieved
        print("You cannot retrieve that from " + names[person] + ".")


def examine(room):
    room["examined"] = True
    if room["examine_items"] != "":
        for item in room["examine_items"]:
            room["visible_items"].append(item)
            room["examine_items"].remove(item)
    print("\nAfter further inspection of the room, you notice some details you had not before.")
    print(room["examine_description"])

def eat(item_id):
    global mass

    for item in inventory:
        if item_id == item["id"]:
            inventory.remove(item)
            remove_mass(item["mass"])
            calculate_stress(item, item["type"])


def light(item_id):
    lit = False
    for item in inventory:
        if item["id"] == "candle" and lit != True and item["type"] != "Light":
            for i in inventory:
                if i["id"] == "matches" and i["amount"] > 0:
                    item["type"] = "Light"
                    item["life"] = 21
                    i["amount"] = i["amount"] - 1
                    lit = True
                    break
                else:
                    print("Matches needed")


def rest():
    global rest_counter
    if rest_counter <= 5:
        for item in current_room["visible_items"]:
            if item["id"] == "bed":
                print("You take a few minutes to rest and collect your thoughts. You can rest a maximus of 5 times")
                calculate_stress(item_bed, "Sleep")
                rest_counter = rest_counter + 1
    else:
        print("You cannot rest now.")


def use(i, object):
    for item in inventory:
        if item["id"] == "key" and object == "painting" and current_room["examined"] == True:
            print("""You put the key into the keyhole on the frame of the painting.
        You turn the key and the painting shifts from the wall. You decide to
        pull and a stairway if revealed hidden behind the painting.""")
            room_living["visible"] = True
            inventory.remove(item)
        elif item["id"] == "book" and current_room["name"] == "The Library" and current_room["examined"] == True:
            room_secret["visible"] = True
            inventory.remove(item)


def execute_command(command, room):
    """
    This function decondes the player input and calls the appropiate function.

    It takes as input the player input.
    """
    try:
        # Checks if command exists
        if 0 == len(command):
            return

        # Checks if command is 'go'
        if command[0] == "go":
            # Checks if command has paramenter
            if len(command) > 1:
                # Executes command
                go(command[1], room)
            else:
                print("Go where?")

        # Checks if command is 'take'
        elif command[0] == "take":
            # Checks if command has paramenter
            if len(command) > 1:
                # Executes command
                take(command[1])
            else:
                print("Take what?")

        # Checks if command is 'drop'
        elif command[0] == "drop":
            # Checks if command has parameter
            if len(command) > 1:
                # Executes command
                drop(command[1])
            else:
                print("Drop what?")

        # Checks if command is 'give'
        elif command[0] == 'give':
            # Checks if command has parameters
            if len(command) > 1:
                # Executes command
                give(command[1], command[2])
            else:
                print("Give what and to who?")

        # Checks if command is 'retrieve'
        elif command[0] == "retrieve":
            # Checks if command has parameters
            if len(command) > 1:
                # Executes command
                retrieve(command[1], command[2])
            else:
                print("Take what and from who?")

        elif command[0] == "examine":
            if len(command) > 0:
                examine(room)
            else:
                print("Examine what?")

        elif command[0] == "eat":
            if len(command) > 1:
                eat(command[1])
            else:
                print("Eat what?")

        elif command[0] == "light":
            if len(command) > 1:
                light(command[1])
            else:
                print("Light what?")

        elif command[0] == "rest":
            if len(command) > 0:
                rest()
            else:
                print("You cannot rest here.")

        elif command[0] == "use":
            if len(command) > 2:
                use(command[1], command[2])
            else:
                print("Use what item on what object?")

        # Checks if command is 'exit'
        elif command[0] == "exit":
            # Executes command
            exit()

        else:
            print("This makes no sense.")
    except TypeError:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    """
    This function prints the menu of available choices to the player, it then takes
    an input an normalizes it.

    It takes as input the exits, room items, inventory items and npc items.
    """
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """
    This function returns the room to which the player will be moving into based
    on the rooms exits and the selected direction.

    It takes as input the exits and direction.
    """
    try:
        # Next room to go to
        return rooms[exits[direction]]
    except KeyError:
        return

def calculate_stress(item, item_type=None):
    """
    This function calculates the player's stress every turn. If it maxes out, the
    player faints and loses their items, or loses. As the stress increases the enemy
    can start to move faster.
    """

    # This makes the function use the global stress variable
    global stress
    global random_num

    if item_type == "Sleep":
        stress = stress - 20
        return

    if item_type == None:
        # Default increase of stress per turn
        stress = stress + random_num + 2

    if item_type == "Food":
        stress = stress - 20

    for item in inventory:
        if item["type"] == "Light":
            stress = stress - random_num

    if stress < 0:
        stress = 0
    return stress


def jumpscare(direction, room):
    global kitchen_scare
    global maze_scare
    global current_room
    global stress

    try:
        if current_room["name"] == "The Start of the Hallway":
            if move(room["exits"], direction)["name"] == "The Kitchen":
                if kitchen_scare == False:
                    stress = stress + 20
                    show_graphic(gargolye)
                    winsound.PlaySound("scream.wav", winsound.SND_FILENAME)
                    kitchen_scare = True
                    current_room = rooms["The Start of the Hallway"]
                    input("PRESS <ENTER> TO CONTINUE")

        if current_room["name"] == "The Living Room":
            if move(room["exits"], direction)["name"] == "The Maze":
                if maze_scare == False:
                    if hatch == True:
                        stress = stress + 20
                        show_graphic(ghost)
                        winsound.PlaySound("scream.wav", winsound.SND_FILENAME)
                        maze_scare = True
                        current_room = rooms["The Living Room"]
                        input("PRESS <ENTER> TO CONTINUE")
    except TypeError:
        pass

def basement_riddle():
    global riddle_answered

    print("The walls start closing in...")

    start = time.time()
    while time.time() - start < 60:
        print("\nRiddle: The Maker doesn't want it, the man who owns it doesnt need it and The person that needs it doesnt know that he needs it. What am i?")
        winsound.PlaySound("backgroundhalloween.wav", winsound.SND_FILENAME)
        answer = input("> ")
        normalised_answer = normalise_input(answer)
        try:
            if normalised_answer[0] != "coffin":
                pass
            else:
                riddle_answered = True
                room_maids["visible"] = True
                room_living["visible"] = True
                return
        except IndexError:
            pass

    print("""Time is up, you got crushed by the walls, a reminder that time is fleeting
    and in real life you have wasted too much and are unalbe to recover it alone.""")
    exit()


def show_graphic(graphic):
    print(graphic)


def save_game():
    """
    This function saves the game when the player wants to quit the game.
    """
    pass


def main():
    global riddle_answered
    global random_num
    global stress

    print("""\n\nYou used to be a 45-year-old very rich entrepreneur. Very recently your business started to fail and you went bankrupt. You lost all of your riches and became depressed. 
You find no reason in living anymore and you feel like giving up. Due to these problems you are often exhausted but still cannot sleep. You decided to take easy way 
out and took some sleeping pills hoping of never waking up again.\n\n""")

    # Main game loop
    while True:

        if stress >= 100:
            print("""You had a heart attack in your real life because you were too stressed. After the event you decide it was time to
            have a better work-life balance""")
            exit()

        random_num = random.randrange(7)

        if maze == True:
            while True:
                if current_maze_room["name"] == "maze_exit":
                    print("""\nYou have managed to escape the maze and snap out of your deep sleep. You collect your thoughts
                    about your life decisions and you remember when your business was just blooming and the joy that brought
                    to your family. You remember when you cared more about your family than your business and riches and know
                    that's how it should be.""")
                    exit()
                for item in inventory:
                    if item["id"] == "map":
                        show_graphic(maze_map)
                command = maze_menu(current_maze_room["exits"])
                execute_command(command, current_maze_room)
                print("Your Stress Level: " + str(stress))
                if maze == False:
                    break

        if current_room["name"] == "The Basement" and riddle_answered == False:
            basement_riddle()

        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        calculate_stress(inventory, None)
        print("Your Stress Level: " + str(stress))
        if stress <= 20:
            print("You're currently Calm")
        elif 20 < stress <= 40:
            print("You're out of your comfort zone")
        elif 40 < stress <= 60:
            print("You're on Edge")
        elif 60 < stress <= 80:
            print("You're Anxious")
        else:
            print("You're very Stressed")

        for item in inventory:
            if item["id"] == "candle" and item["life"] > 0 and item["type"] == "Light":
                item["life"] = item["life"] - 1
                calculate_stress(inventory, item["type"])
            if item["id"] == "candle" and item["life"] == 1:
                inventory.remove(item)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["visible_items"], inventory)

        # Execute the player's command
        execute_command(command, current_room)

        print("\n-----------------------------------------------------------------------------------------------------------------------------")

        """
        WIN CONDITION 1
        """
        for i in inventory:
            if current_room["name"] == "The Attic" and i["id"] == "phone":
                print("""Your phone buzzes and you see you got a text from your partner asking if your going to be working late again.
Realizing how much you miss your partner you eagerly respond that your coming home soon. You also realize
that your love for one another and your love for your children outweighs the loss of wealth and riches and
is not as important as your family in your life.""")
                exit()


if __name__ == "__main__":
    main()
