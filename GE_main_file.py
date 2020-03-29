import random
import GE_dicts_objects

world = {
    "security_door": "Locked",
    "storage_light": "Off",
    "laser_array": "On",
    "elevator": "Off",
    "elevator_called": False
}

player = {
    "Name": "Unknown",
    "Inventory": [],
    "position": {
        "x_axis": 5,
        "y_axis": 1
    }
}

all_possible_coordinates = [
    (5, 1),  # holding room, first location
    (5, 2),  # hallway with security door
    (4, 2),  # storage room containing various chemical compounds
    # (5, 3),    # hallway, added to this list once security door = "open"
    (4, 3),  # security room, high hacking can disable laser array
    (5, 4),  # monitored corridor with harmful laser arrays
    (6, 4),  # warden's quarters, personal notes reveal elevator password
    (5, 5),  # elevator
]


def wrong_input():
    input("\nSorry, wrong input, press ENTER to try again.\n")


# CHARACTER SET UP #----------------------------------------------------------------------------------------------------


def set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name):   # setting up skills one by one
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
        print("\nYou have unused points!!!\n")


def skills_setup(total_points, skill_min, skill_max, skill_list, skillset_name):
    input("\nMinimum of 0 and a maximum of " + str(skill_max - 1) + " can be devoted to a skill. Press ENTER.\n")
    set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name)


def set_up_review(player_dict_segment):                          # reviewing skills and asking if continue or start over
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


def full_character_setup():              # full character creation func, can contain more generic functions with attribs
    ready = False
    while ready is False:
        skills_setup(12, 1, 5, GE_dicts_objects.skill_list, "Skills")
        ready = set_up_review(player["Skills"])


# GAME INTERACTABLE OBJECTS #-------------------------------------------------------------------------------------------


def cryo_chamber():                                                              # other cryogenic chamber in first room
    input(GE_dicts_objects.objects["cryo_chamber"]["input1"])
    input(GE_dicts_objects.objects["cryo_chamber"]["input2"])


def log_terminal():                     # computer terminal in first room - contains email containing security door code
    input(GE_dicts_objects.objects["log_terminal"]["input1"])
    if "Skills" in player.keys() and "Hacking" in player["Skills"].keys() and player["Skills"]["Hacking"] >= 4:
        input(GE_dicts_objects.objects["log_terminal"]["input2"])
        while True:
            choice = int(input("\nPress 1 to view random email\nPress 2 to exit\n"))
            try:
                if choice == 1:
                    print(random.choice(GE_dicts_objects.email_list))
                elif choice == 2:
                    break
            except ValueError:
                wrong_input()
    else:
        input(GE_dicts_objects.objects["log_terminal"]["input3"])


def keypad(pincode):                                       # keypad in first hallway - used to open door once code known
    global world
    global all_possible_coordinates
    ans = str(input(GE_dicts_objects.objects["keypad"]["input1"]))
    if ans == str(pincode):
        world["security_door"] = "Open"
        all_possible_coordinates.append((5, 3))
        print(GE_dicts_objects.objects["keypad"]["input2"])
    else:
        input("Nothing happens.")


def security_door():                                          # security door in first hallway leading to second hallway
    global world
    global all_possible_coordinates
    if world["security_door"] == "Locked":
        input(GE_dicts_objects.objects["security_door"]["input1"])
        while True:
            if "Skills" in player.keys() and "Strength" in player["Skills"].keys() and \
                    player["Skills"]["Strength"] >= 5:
                print("Press 'F' to force the door open.")
                str = True
            if "Skills" in player.keys() and "Mechanics" in player["Skills"].keys() and \
                    player["Skills"]["Mechanics"] >= 4:
                print("Press 'M' to tinker with the opening mechanism and electronics.")
                mech = True
            if "Skills" in player.keys() and "Science" in player["Skills"].keys() and \
                    player["Skills"]["Science"] >= 5:
                print("Press 'S' to blow up the lock with an improvised explosive charge.")
                sci = True
            choice = (input("Press 1 use keypad\nPress 2 to exit\n")).lower()
            try:
                if choice == "1":
                    keypad(GE_dicts_objects.code_this_iteration)
                    break
                elif choice == "2":
                    break
                elif choice == "f" and str is True:
                    world["security_door"] = "Open"
                    all_possible_coordinates.append((5, 3))
                    print(GE_dicts_objects.objects["security_door"]["input2"])
                    break
                elif choice == "m" and mech is True:
                    world["security_door"] = "Open"
                    all_possible_coordinates.append((5, 3))
                    print(GE_dicts_objects.objects["security_door"]["input3"])
                    break
                elif choice == "s" and sci is True:
                    if "volatile chemicals" in player["Inventory"]:
                        world["security_door"] = "Open"
                        all_possible_coordinates.append((5, 3))
                        print(GE_dicts_objects.objects["security_door"]["input4"])
                        break
                    else:
                        print(GE_dicts_objects.objects["security_door"]["input5"])
            except ValueError:
                wrong_input()
    else:
        input(GE_dicts_objects.objects["security_door"]["input6"])


def shipping_manifest():
    return True

def volatile_chem():
    return True

# NAMES OF ALL INTERACTABLE OBJECT - REQUIRED FOR ROOM TO WORK # -------------------------------------------------------


object_names = {
    cryo_chamber: "cryogenic chamber",
    log_terminal: "computer terminal",
    security_door: "security door"
}


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


# MAIN GAME MECHANICS - LOCATION # -------------------------------------------------------------------------------------


def room(name, intro, *objects_to_interact):
    print("\nThis appears to be a " + name + ".")
    print(intro + "\n")
    objects_in_room = []
    object_signatures = {}
    for obj in objects_to_interact:
        objects_in_room.append(obj)
    for obj in objects_in_room:
        object_signatures[obj] = int(objects_in_room.index(obj) + 1)
    while True:
        try:
            for obj in objects_in_room:
                print("Press " + str(object_signatures[obj]) +
                      " to interact with the " + object_names[obj])
            print("Press 0 to exit room.\n")
            choice = int(input(""))
            if choice in object_signatures.values():
                (list(object_signatures.keys())[list(object_signatures.values()).index(choice)])()
            elif choice == 0:
                break
            else:
                wrong_input()
        except ValueError:
            wrong_input()
    relocate()


# MAIN GAME MECHANICS - CALLING ROOMS BASED ON LOCATION # --------------------------------------------------------------


def the_game():
    input(GE_dicts_objects.locations["main"]["intro"])
    global player
    global world
    while world["elevator_called"] is False:
        current_position = (player["position"]["x_axis"], player["position"]["y_axis"])
        if current_position == (5, 1):
            room("holding room", GE_dicts_objects.locations["holding_room"]["intro"], cryo_chamber, log_terminal)
        elif current_position == (5, 2):
            room("hallway", GE_dicts_objects.locations["hallway"]["intro"], security_door)
        elif current_position == (4, 2):
            room("storage room", GE_dicts_objects.locations["storage_room"]["intro"], shipping_manifest, volatile_chem)
        elif current_position == (5, 3):
            room("hallway junction", GE_dicts_objects.locations["hallway_junction"]["intro"])
        elif current_position == (4, 3):  # security room
            print("sec room")
        elif current_position == (5, 4):  # monitored corridor
            print("sec room")
        elif current_position == (6, 4):  # warden's quarters
            print("sec room")
        elif current_position == (5, 5):  # elevator
            print("sec room")
    input("Press ENTER to quit.")


full_character_setup()
the_game()
