
def wrong_input():
    input("\nSorry, wrong input, press ENTER to try again.\n")


def insufficient_skill():
    input("You don\'t have the skills necessary to use this." "\n")


def list_contents(contents_dict):
    for item in contents_dict:
        if contents_dict[item] > 0:
            print(item + " x " + str(contents_dict[item]))
        else:
            pass
    print("\n")


def skill_check(player_obj, skill, skill_lvl):
    if skill in player_obj.skills and \
            player_obj.skills[skill] >= skill_lvl:
        print("Press 'S' to use your " + skill + " skill.")
    else:
        insufficient_skill()


def item_check(player_obj, item):
    if item in player_obj.inventory:
        print("Press 'I' to use  " + item + " on this object.")


starting_position = {
    "x_axis": 5,
    "y_axis": 1
}

