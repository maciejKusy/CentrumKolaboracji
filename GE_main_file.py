import random
import GE_dicts_objects

world = {
    "holding_room1": {  # World Locations
        "communication terminal": 1,  # Objects in each location - '1' means either 'on' of 'locked'
        "portable ChemLab": 0,
        "DeepSleep chamber #2": {
            "lock_status": 0,
            "contents": ["Fusion Cell"]
        },
        "Warning poster": 1
    },
    "holding_room2": {
        "DeepSleep chamber #3": {
            "lock_status": 0,
            "contents": ["Fusion Cell"]
        },
        "Air Vent": 0
    },
    "hallway1": {
        "security door": 1
    },
    "storage_room": {
        "shelf": {
            "lock_status": 0,
            "contents": ["Bottle of V-084", "Bottle of C3H8O3", "Steel Canister", "Bottle of H2O", "Bottle of V-66",
                         "Bottle of C2H5OH", "Pink, unmarked bottle"]
        },
        "tool closet": {
            "lock_status": 1,
            "contents": ["Screwdriver", "Broomstick"]
        }
    },
    "hallway2": None,
    "security_room": {
        "security terminal": 1,
        "prisoner shipping manifest": 1
    },
    "microwave_array_corridor": {
        "microwave_array": None,
    },
    "elevator": "Off",
    "elevator_called": False
}

player = {
    "Name": [],
    "Inventory": [],
    "Crafting Recipes": [],
    "position": {
        "x_axis": 5,
        "y_axis": 1
    }
}

all_possible_coordinates = [
    (5, 1),  # holding room, first location
    (5, 2),  # hallway with security door
    (4, 2),  # storage room - volatile chemicals + metal rod
    (6, 1),  # second holding room - cryo_chamber containing battery
    # (5, 3)    # hallway, added to this list once security door is opened
    # (4, 3)    # security room, high hacking can disable laser array
    (5, 4),    # monitored corridor with harmful laser arrays
    (6, 4),  # warden's quarters, personal notes reveal elevator password
    # (5, 5),  # elevator
]


def wrong_input():
    input("\nSorry, wrong input, press ENTER to try again.\n")


# CHARACTER SET UP #----------------------------------------------------------------------------------------------------


def set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name):  # setting up skills one by one
    global player
    total = total_points - (len(skill_list) * skill_min)
    player[skillset_name] = {}
    for s in skill_list:
        player[skillset_name][s] = skill_min
    for s in skill_list:
        skill_value = 0
        while True:
            try:
                print("You got " + str(total) + " points left.")
                answer = int(input("\nAssign points to " + str(s) + ".\n"))
                if answer <= total:
                    if 0 <= answer <= (skill_max - skill_min):
                        skill_value += answer
                        total -= answer
                        break
                    else:
                        print("\nPlease select value between 0 and " + str(skill_max - skill_min) + ".\n")
                        continue
                else:
                    print("\nNot enough points. You got " + str(total) + " points.\n")
            except ValueError:
                wrong_input()
                continue
        player[skillset_name][s] += skill_value
    if total > 0:
        print("\nYOU HAVE UNUSED POINTS!!! YOU MIGHT HAVE CREATED A LAME CHARACTER!!!\n")


def skills_setup(total_points, skill_min, skill_max, skill_list, skillset_name):
    input("Minimum of 0 and a maximum of " + str(skill_max - 1) + " can be devoted to a skill.\n")
    input("It is recommended to set at least one skill to 5 and one to 1. Press ENTER.\n")
    set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name)


# reviewing skills and asking if continue or start over
def set_up_review(player_dict_segment):
    ready = None
    while True:
        for key in player_dict_segment:
            print(key + " : " + str(player_dict_segment[key]))
        answer = (input("\nPress Y to proceed and N to re-set.\n")).lower()
        if answer == "y":
            ready = True
            break
        elif answer == "n":
            ready = False
            break
        else:
            wrong_input()
            continue
    return ready


# full character creation func, can contain more generic functions with attribs
def full_character_setup():
    ready = False
    while ready is False:
        skills_setup(12, 1, 5, GE_dicts_objects.skill_list, "Skills")
        ready = set_up_review(player["Skills"])


# GAME INTERACTABLE OBJECTS #-------------------------------------------------------------------------------------------


# function for random objects containing information, sometimes influencing Player
def object_info(world_location, world_object_affected, intro, player_char_affected, *additions_to_player_char):
    global world
    global player
    print(intro + "\n")
    if world[world_location][world_object_affected] == 1:
        for addition in additions_to_player_char:
            player[player_char_affected].append(addition)
            print(addition + " has been added to your " + player_char_affected)
        world[world_location][world_object_affected] = 0
        print("\n")
    else:
        input("Nothing more to do here.\n")


# function to turn on any crafting station should it be powered down
def turning_on_craftstation(world_location, world_object_affected, power_source):
    global world
    global player
    if world[world_location][world_object_affected] == 0:
        print(GE_dicts_objects.objects["craftstation"]["input1"] + "\n")
        input(GE_dicts_objects.objects["craftstation"]["input2"] + "\n")
        if power_source in player["Inventory"]:
            input(GE_dicts_objects.objects["craftstation"]["input5"] + power_source)
            player["Inventory"].remove(power_source)
            world[world_location][world_object_affected] = 1
        else:
            input(GE_dicts_objects.objects["craftstation"]["input6"])
    else:
        input(GE_dicts_objects.objects["craftstation"]["input3"] + "\n")


# crafting function based on list of crafting recipes
def crafting(crafting_recipe_list):
    global player
    items_used = []
    input("Select a known crafting recipe:\n")
    known_recipes = player["Crafting Recipes"]
    if len(known_recipes) != 0:
        for recipe in known_recipes:
            print("Press " + str(known_recipes.index(recipe) + 1) + " to craft " + recipe)
    else:
        input("You don\'t know any usable recipes.")
        return
    choice = int(input(""))
    selected_recipe = known_recipes[(choice - 1)]
    while True:
        available_items = player["Inventory"]
        for item in available_items:
            print("Press " + str(available_items.index(item) + 1) + " to add " + item)
        try:
            selection = int(input("Press '9' to craft, press '0' to exit.\n"))
            if selection < 9 and selection != 0:
                selected_item = available_items[(selection - 1)]
                items_used.append(selected_item)
                player["Inventory"].remove(selected_item)
                continue
            elif selection == 9:
                items_used.sort()
                if items_used == crafting_recipe_list[selected_recipe]:
                    player["Inventory"].append(selected_recipe)
                    input("You crafted a " + selected_recipe + ".\n")
                    break
                else:
                    for item in items_used:
                        items_used.remove(item)
                        player["Inventory"].append(item)
                    input("You failed to craft a " + selected_recipe + ".\n")
                    break
            elif selection == 0:
                break
        except:
            wrong_input()


# function to operate crafting station - TO BE RE-DONE with a proper crafting system
def object_craftstation(world_location, world_object_affected, intro, power_source, skill_required, skill_lvl_required,
                        crafting_recipe_list):
    global world
    global player
    print(intro + "\n")
    turning_on_craftstation(world_location, world_object_affected, power_source)
    if world[world_location][world_object_affected] == 0:
        return
    else:
        if "Skills" in player.keys() and skill_required in player["Skills"].keys() and \
                player["Skills"][skill_required] >= skill_lvl_required:
            crafting(crafting_recipe_list)
        else:
            input(GE_dicts_objects.objects["craftstation"]["input4"] + "\n")


# function for hacking any terminal - will be embedded in any terminal function
def hacking_terminal(world_location, world_object_affected, skill_lvl_required):
    global world
    global player
    if world[world_location][world_object_affected] == 1:
        print(GE_dicts_objects.objects["terminal"]["input4"] + "\n")
        input(GE_dicts_objects.objects["terminal"]["input2"] + "\n")
        while True:
            if "Skills" in player.keys() and "Hacking" in player["Skills"].keys() and \
                    player["Skills"]["Hacking"] >= skill_lvl_required:
                print(GE_dicts_objects.objects["terminal"]["input5"])
                choice = (input("Press '0' to exit.\n")).lower()
                try:
                    if choice == '0':
                        break
                    elif choice == 'h' and player["Skills"]["Hacking"] >= skill_lvl_required:
                        input(GE_dicts_objects.objects["terminal"]["input6"] + "\n")
                        world[world_location][world_object_affected] = 0
                        break
                except ValueError:
                    wrong_input()
            else:
                input(GE_dicts_objects.objects["terminal"]["input8"] + "\n")
                break
    else:
        input(GE_dicts_objects.objects["terminal"]["input7"] + "\n")


# function for interacting with a computer terminal that contains data files for reading
def object_terminal(world_location, world_object_affected, intro, skill_lvl_required, data_list, data_list_name):
    global player
    global world
    print(intro + "\n")
    hacking_terminal(world_location, world_object_affected, skill_lvl_required)
    if world[world_location][world_object_affected] == 1:
        return
    else:
        while True:
            choice = (input("Press 1 to view " + data_list_name + ".\nPress '0' to exit.\n"))
            try:
                if choice == '1':
                    print(random.choice(data_list))
                elif choice == '0':
                    break
            except ValueError:
                wrong_input()


# function for a keypad -- embedded in the security door function will open certain locations if code correct
def object_keypad(world_location, world_object_affected, pin, *locations_opened):
    global world
    global all_possible_coordinates
    ans = str(input(GE_dicts_objects.objects["keypad"]["input1"]))
    if ans == str(pin):
        world[world_location][world_object_affected] = 0
        for location in locations_opened:
            all_possible_coordinates.append(location)
        print(GE_dicts_objects.objects["keypad"]["input2"])
    else:
        input("Code incorrect.")


# function for security door with keypad - 3 ways to open: pin / skill / item
def object_security_door(world_location, world_object_affected, intro, pin, skill_required, skill_lvl_required,
                         skill_open_message, usable_item, item_open_message, *locations_opened):
    global world
    global player
    global all_possible_coordinates
    print(intro + "\n")
    if world[world_location][world_object_affected] == 1:
        while True:
            if "Skills" in player.keys() and skill_required in player["Skills"].keys() and \
                    player["Skills"][skill_required] >= skill_lvl_required:
                print("Press 'S' to use your " + skill_required + " skills to open this door.")
            elif usable_item in player["Inventory"]:
                print("Press 'I' to use  " + usable_item + " to open this door.")
            choice = (input("Press 1 to use keypad.\nPress '0' to exit.\n"))
            try:
                if choice == 's' and player["Skills"][skill_required] >= skill_lvl_required:
                    input(skill_open_message + "\n")
                    world[world_location][world_object_affected] = 0
                    for location in locations_opened:
                        all_possible_coordinates.append(location)
                    break
                elif choice == 'i' and usable_item in player["Inventory"]:
                    input(item_open_message + "\n")
                    world[world_location][world_object_affected] = 0
                    for location in locations_opened:
                        all_possible_coordinates.append(location)
                    break
                elif choice == '1':
                    object_keypad(world_location, world_object_affected, pin, *locations_opened)
                    break
                elif choice == '0':
                    break
            except ValueError:
                wrong_input()
    else:
        input(GE_dicts_objects.objects["security_door"]["input4"])


# function for retrieving items from container based on contents of object in 'world' dict
def retrieving_items_from_container(world_location, world_object_affected):
    global world
    global player
    while True:
        contents = world[world_location][world_object_affected]["contents"]
        try:
            for item in contents:
                print("Press " + str(contents.index(item) + 1) + " to take " + item + ".")
            choice = int(input("Press 9 to take all.\nPress '0' to exit.\n"))
            if choice in range(len(contents) + 1) and choice != 0:
                selection = contents[choice - 1]
                player["Inventory"].append(selection)
                world[world_location][world_object_affected]["contents"].remove(selection)
                print(str(selection) + " added to Inventory.\n")
                break
            elif choice == 9:
                for item in contents:
                    player["Inventory"].append(item)
                    print(item + " added to Inventory.\n")
                world[world_location][world_object_affected]["contents"] = []
                break
            elif choice == 0:
                break
        except ValueError:
            wrong_input()


# generic function for objects that are item containers based on objects in the 'world' dict
def object_container(world_location, world_object_affected, intro, skill_required,
                     skill_lvl_required, skill_open_message, usable_item, item_open_message):
    global world
    global player
    print(intro + "\n")
    if world[world_location][world_object_affected]["lock_status"] == 1:
        input(GE_dicts_objects.objects["container"]["locked"])
        while True:
            if "Skills" in player.keys() and skill_required in player["Skills"].keys() and \
                    player["Skills"][skill_required] >= skill_lvl_required:
                print("Press 'S' to use your " + skill_required + " skills to open this container.")
            elif usable_item in player["Inventory"]:
                print("Press 'I' to use  " + usable_item + " to open this container.")
            choice = (input("Press '0' to exit.\n"))
            try:
                if choice == 's' and player["Skills"][skill_required] >= skill_lvl_required:
                    input(skill_open_message + "\n")
                    world[world_location][world_object_affected]["lock_status"] = "Unlocked"
                    input("The contents are:\n")
                    for item in world[world_location][world_object_affected]["contents"]:
                        print(item)
                    print("\n")
                    retrieving_items_from_container(world_location, world_object_affected)
                    break
                elif choice == 'i' and usable_item in player["Inventory"]:
                    input(item_open_message + "\n")
                    world[world_location][world_object_affected]["lock_status"] = 0
                    input("The contents are:\n")
                    for item in world[world_location][world_object_affected]["contents"]:
                        print(item)
                    print("\n")
                    retrieving_items_from_container(world_location, world_object_affected)
                    break
                elif choice == '0':
                    break
            except ValueError:
                wrong_input()
    elif world[world_location][world_object_affected]["lock_status"] == 0:
        print(GE_dicts_objects.objects["container"]["open"])
        if len(world[world_location][world_object_affected]["contents"]) != 0:
            input("The contents are:\n")
            for item in world[world_location][world_object_affected]["contents"]:
                print(item)
            retrieving_items_from_container(world_location, world_object_affected)
        else:
            input("It is empty.\n")


def object_ventilation_shaft(world_location, world_object_affected, intro, fitness_lvl_required,
                             exit_location):
    global world
    global player
    print(intro + "\n")
    fit_enough = False
    if "Skills" in player.keys() and "Fitness" in player["Skills"].keys() and \
            player["Skills"]["Fitness"] >= fitness_lvl_required:
        fit_enough = True
        print("Press 1 to enter the vent.")

    print("Press '0' to exit.\n")
    choice = int(input(""))
    try:
        if choice == 1 and fit_enough is True:
            input(GE_dicts_objects.objects["random"]["inside_vent1"] + "\n")
            input(GE_dicts_objects.objects["random"]["inside_vent2"] + "\n")
            player["position"]["x_axis"] = exit_location[0]
            player["position"]["y_axis"] = exit_location[1]
        elif choice == 0:
            return
    except ValueError:
        wrong_input()


def object_movement_obstacle_10step(world_location, world_object_affected, intro, msg_failure, location_opened,
                                    combination):
    global world
    print(intro + "\n")
    move1 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
    if move1 == combination[0]:
        move2 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
        if move2 == combination[1]:
            move3 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
            if move3 == combination[2]:
                move4 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                if move4 == combination[3]:
                    move5 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                    if move5 == combination[4]:
                        move6 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                        if move6 == combination[5]:
                            move7 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                            if move7 == combination[6]:
                                move8 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                                if move8 == combination[7]:
                                    move9 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                                    if move9 == combination[8]:
                                        move10 = input("""Press 'W' to move forward
Press 'S' to move backwards
Press 'A' to move left
Press 'D' to move right\n""").lower()
                                        if move10 == combination[9]:
                                            all_possible_coordinates.append(location_opened)
                                            print("You manage to navigate the obstacle and can now move past it.\n")
                                        else:
                                            print(msg_failure + "\n")
                                            return
                                    else:
                                        print(msg_failure + "\n")
                                        return
                                else:
                                    print(msg_failure + "\n")
                                    return
                            else:
                                print(msg_failure + "\n")
                                return
                        else:
                            print(msg_failure + "\n")
                            return
                    else:
                        print(msg_failure + "\n")
                        return
                else:
                    print(msg_failure + "\n")
                    return
            else:
                print(msg_failure + "\n")
                return
        else:
            print(msg_failure + "\n")
            return
    else:
        print(msg_failure + "\n")
        return

# MAIN GAME MECHANICS - RELOCATION #------------------------------------------------------------------------------------


def relocate():
    global player
    choices = []
    if (player["position"]["x_axis"] + 1, player["position"]["y_axis"]) in all_possible_coordinates:
        choices.append("e")
        print("Press 'E' to go east;")
    if (player["position"]["x_axis"] - 1, player["position"]["y_axis"]) in all_possible_coordinates:
        choices.append("w")
        print("Press 'W' to go west;")
    if (player["position"]["x_axis"], player["position"]["y_axis"] + 1) in all_possible_coordinates:
        choices.append("n")
        print("Press 'N' to go north;")
    if (player["position"]["x_axis"], player["position"]["y_axis"] - 1) in all_possible_coordinates:
        choices.append("s")
        print("Press 'S' to go south;")
    while True:
        direction = (input("Select direction:\n")).lower()
        if direction == "n":
            player["position"]["y_axis"] = player["position"]["y_axis"] + 1
            break
        elif direction == "e":
            player["position"]["x_axis"] = player["position"]["x_axis"] + 1
            break
        elif direction == "s":
            player["position"]["y_axis"] = player["position"]["y_axis"] - 1
            break
        elif direction == "w":
            player["position"]["x_axis"] = player["position"]["x_axis"] - 1
            break
        elif direction not in choices:
            wrong_input()


# ROOMS IN GAME #  ----------------------------------------------------------------------------------------------------


def lvl1_room_holding_room1(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_terminal(world_location, "communication terminal",
                                GE_dicts_objects.objects["terminal"]["input1"], 4,
                                GE_dicts_objects.messages_list, "messages")
            elif choice == 2:
                object_craftstation(world_location, "portable ChemLab",
                                    GE_dicts_objects.objects["craftstation"]["intro_chemlab"], "Fusion Cell",
                                    "Science", 5, GE_dicts_objects.ChemLab_crafting_recipes)
            elif choice == 3:
                object_container(world_location, "DeepSleep chamber #2",
                                 GE_dicts_objects.objects["container"]["intro_DeepSleep_chamber_#2"], None, None,
                                 None, None, None)
            elif choice == 4:
                object_info(world_location, "Warning poster",
                            GE_dicts_objects.objects["random"]["intro_holding1_poster"], "Crafting Recipes",
                            "Small Explosive Device")
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_hallway1(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_security_door(world_location, "security door",
                                     GE_dicts_objects.objects["security_door"]["input1"],
                                     GE_dicts_objects.code_this_iteration,
                                     "Electronics", 5, GE_dicts_objects.objects["security_door"]["input2mech"],
                                     "Small Explosive Device", GE_dicts_objects.objects["security_door"]["input3expl"],
                                     (5, 3), (4, 3))
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_holding_room2(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_container(world_location, "DeepSleep chamber #3",
                                 GE_dicts_objects.objects["container"]["intro_DeepSleep_chamber_#3"], None,
                                 None, None, None, None)
            elif choice == 2:
                object_ventilation_shaft(world_location, "Air Vent",
                                         GE_dicts_objects.objects["random"]["intro_vent_generic"], 5, (6, 4))
                return
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_storage_room(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_container(world_location, "shelf",
                                 GE_dicts_objects.objects["container"]["intro_chemshelf"], None,
                                 None, None, None, None)
            elif choice == 2:
                object_container(world_location, "tool closet",
                                 GE_dicts_objects.objects["container"]["intro_tool_closet"], "Electronics",
                                 3, GE_dicts_objects.objects["container"]["open_electronics"], None, None)
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_hallway2(intro, world_location):
    print(intro + "\n")
    while True:
        try:
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_security_room(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_terminal(world_location, "security terminal", GE_dicts_objects.objects["terminal"]["input1"], 5,
                                GE_dicts_objects.security_notes_list, "security notes")
            elif choice == 2:
                object_info(world_location, "prisoner shipping manifest",
                            GE_dicts_objects.objects["random"]["intro_prisoner_manifest"], "Name", "Detainee #562E")
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


def lvl1_room_microwave_array(intro, world_location):
    print(intro + "\n")
    objects_in_room = list(world[world_location].keys())
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(objects_in_room.index(obj) + 1) +
                      " to interact with the " + obj)
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice == 1:
                object_movement_obstacle_10step(world_location, "microwave_array",
                                                GE_dicts_objects.objects["random"]["array_intro"],
                                                GE_dicts_objects.objects["random"]["array_failure"], (5, 5),
                                                "wddwasaasw")
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


# MAIN GAME MECHANICS - CALLING ROOMS BASED ON LOCATION # --------------------------------------------------------------


def game_sub_level_1():
    input(GE_dicts_objects.locations["main"]["intro"])
    global player
    global world
    while world["elevator_called"] is False:
        current_position = (player["position"]["x_axis"], player["position"]["y_axis"])
        if current_position == (5, 1):
            lvl1_room_holding_room1(GE_dicts_objects.locations["holding_room1"]["intro"], "holding_room1")
        elif current_position == (5, 2):  # hallway1
            lvl1_room_hallway1(GE_dicts_objects.locations["hallway1"]["intro"], "hallway1")
        elif current_position == (6, 1):  # holding_room2
            lvl1_room_holding_room2(GE_dicts_objects.locations["holding_room2"]["intro"], "holding_room2")
        elif current_position == (4, 2):  # storage_room
            lvl1_room_storage_room(GE_dicts_objects.locations["storage_room"]["intro"], "storage_room")
        elif current_position == (5, 3):  # hallway2
            lvl1_room_hallway2(GE_dicts_objects.locations["hallway2"]["intro"], "hallway2")
        elif current_position == (4, 3):  # security room
            lvl1_room_security_room(GE_dicts_objects.locations["security_room"]["intro"], "security_room")
        elif current_position == (5, 4):  # monitored corridor
            lvl1_room_microwave_array(GE_dicts_objects.locations["microwave_array"]["intro"],
                                      "microwave_array_corridor")
        elif current_position == (6, 4):  # warden's quarters
            print("warden\'s quarter")
        elif current_position == (5, 5):  # elevator
            print("not ready yet")
    input("Press ENTER to move onwards.")


full_character_setup()
game_sub_level_1()
