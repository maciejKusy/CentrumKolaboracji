import random
import HerzDungDicts

all_possible_coordinates = [(2, 2), (2, 1), (1, 2), (3, 2), (2, 3)]


def display_incorrect_input():
    print("Sorry, wrong input.\n\n")


def hall_room(player):
    print("This is the hall. Nothing here but four doors... That\'s weird.\n\n")
    return relocate(player)


def videotape_room(player):
    print(HerzDungDicts.rooms["videotape_room"]["intro"])
    choices = HerzDungDicts.rooms["videotape_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["videotape_room"]["input_message"])).lower()
        if answer not in choices:
            display_incorrect_input()
        elif answer == "a":
            print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["watching_tv"] +
                  random.choice(list(HerzDungDicts.tv_programmes.values())))
        elif answer == "b":
            if not player["has_found_videotape"]:
                player["has_found_videotape"] = True
                print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["first_search"])
            else:
                print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["further_searches"])
        elif answer == "c":
            return relocate(player)


def sadness_room(player):
    print(HerzDungDicts.rooms["sadness_room"]["intro"])
    choices = HerzDungDicts.rooms["sadness_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["sadness_room"]["input_message"])).lower()
        if answer not in choices:
            display_incorrect_input()
        elif answer == "a":
            if not player["has_induced_sadness"]:
                player["has_induced_sadness"] = True
                print(HerzDungDicts.rooms["sadness_room"]["action_messages"]["first_sadness"])
            else:
                print(HerzDungDicts.rooms["sadness_room"]["action_messages"]["further_sadness"])
        elif answer == "b":
            return relocate(player)


def key_room(player):
    print(HerzDungDicts.rooms["key_room"]["intro"])
    choices = HerzDungDicts.rooms["key_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["key_room"]["input_message"])).lower()
        if answer not in choices:
            display_incorrect_input()
        elif answer == "a":
            if not player["has_found_key"]:
                player["has_found_key"] = True
                print(HerzDungDicts.rooms["key_room"]["action_messages"]["first_key_search"])
            else:
                print(HerzDungDicts.rooms["key_room"]["action_messages"]["further_key_search"])
        elif answer == "b":
            return relocate(player)


def herzog_room(player):
    global all_possible_coordinates
    if not player["has_defeated_herzog"]:
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat1"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat2"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat3"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat4"])
        choices = HerzDungDicts.rooms["herzog_room"]["choices"]
        while True:
            answer = (input(HerzDungDicts.rooms["herzog_room"]["input_message_pre_defeat"])).lower()
            if answer not in choices:
                display_incorrect_input()
            elif answer == "a":
                print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["attack"])
            elif answer == "b":
                if player["has_found_videotape"] and player["has_induced_sadness"]:
                    all_possible_coordinates.append((2, 4))
                    player["has_defeated_herzog"] = True
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["smart_defeat"])
                    return player
                elif player["has_found_videotape"]:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["videotape_only"])
                elif player["has_induced_sadness"]:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["sadness_only"])
                else:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["unprepared"])
            else:
                return relocate(player)
    else:
        print(HerzDungDicts.rooms["herzog_room"]["intro_post_defeat"])
        while True:
            answer = (input(HerzDungDicts.rooms["herzog_room"]["input_message_post_defeat"])).lower()
            if answer != "a":
                display_incorrect_input()
            else:
                return relocate(player)


def exit_room(player):
    print(HerzDungDicts.rooms["exit_room"]["intro"])
    choices = HerzDungDicts.rooms["exit_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["exit_room"]["input_message"])).lower()
        if answer not in choices:
            display_incorrect_input()
        elif answer == "a":
            if player["has_found_key"]:
                player["is_ready_to_leave"] = True
                print(HerzDungDicts.rooms["exit_room"]["action_messages"]["key_found"])
                return player
            else:
                print(HerzDungDicts.rooms["exit_room"]["action_messages"]["key_not_found"])
        elif answer == "b":
            return relocate(player)


def find_possible_moves(player):
    return True


def relocate(player):
    choices = []
    if get_position(player, 1) in all_possible_coordinates:
        choices.append("e")
        print("Press 'E' to go east;")
    if get_position(player, -1) in all_possible_coordinates:
        choices.append("w")
        print("Press 'W' to go west;")
    if get_position(player, 0, 1) in all_possible_coordinates:
        choices.append("n")
        print("Press 'N' to go north;")
    if get_position(player, 0, -1) in all_possible_coordinates:
        choices.append("s")
        print("Press 'S' to go south;")
    while True:
        direction = (input("Select direction:\n")).lower()
        if direction not in choices:
            display_incorrect_input()
            continue
        elif direction == "n":
            player["position"]["y_axis"] = player["position"]["y_axis"] + 1
        elif direction == "e":
            player["position"]["x_axis"] = player["position"]["x_axis"] + 1
        elif direction == "s":
            player["position"]["y_axis"] = player["position"]["y_axis"] - 1
        elif direction == "w":
            player["position"]["x_axis"] = player["position"]["x_axis"] - 1

        return player


def prepare_rooms():
    return {
        (2, 2): hall_room,
        (2, 1): sadness_room,
        (1, 2): videotape_room,
        (3, 2): key_room,
        (2, 3): herzog_room,
        (2, 4): exit_room
    }


def prepare_player():
    return {
        "position": {
            "x_axis": 2,
            "y_axis": 2
        },
        "has_defeated_herzog": False,
        "has_found_videotape": False,
        "has_induced_sadness": False,
        "has_found_key": False,
        "is_ready_to_leave": False
    }


def get_position(player, mod_x=0, mod_y=0):
    return player["position"]["x_axis"] + mod_x, player["position"]["y_axis"] + mod_y


def the_game():
    input("Welcome to the dungeon. Press ENTER to dive head-first into madness...")
    rooms = prepare_rooms()
    player = prepare_player()
    while not player["is_ready_to_leave"]:
        current_position = get_position(player)
        player = rooms[current_position](player)

    choice = input("Type P to play again, or any other key to exit\n")
    if choice == 'A':
        the_game()
    else:
        print('The end')


the_game()
