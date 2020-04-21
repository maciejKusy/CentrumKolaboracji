
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


starting_position = {
    "x_axis": 5,
    "y_axis": 1
}





