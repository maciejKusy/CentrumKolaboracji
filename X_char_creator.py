
# available_classes = {
#     'fighter': {
#         'starting_inv': {
#             'short sword': 1,
#             'wooden shield': 1,
#             'small health potion': 1
#         }
#     },
#     'thief': {
#         'starting_inv': {
#             'dagger': 1,
#             'leather hood': 1,
#             'lockpick': 1
#         }
#     },
#     'wizard': {
#         'starting_inv': {
#             'gnarly staff': 1,
#             'woolen robe': 1,
#             'mana potion': 1
#         }
#     }
# }

# available_classes_list = list(available_classes.keys())
available_sexes = ['male', 'female', 'transsexual']
available_races = ['human', 'marxist', 'gypsy']
available_skills = ["Science", "Hacking", "Electronics", "Fitness"]


def wrong_input():
    input("\nSorry, wrong input, press ENTER to try again.\n")


# def set_parameter_from_input(parameter_name):
#     choice = input("Enter your hero\'s " + parameter_name + ":\n").capitalize()
#     return choice


def set_parameter_from_list(parameter_name, parameter_list):
    while True:
        try:
            print("Select your hero\'s " + parameter_name + ":\n")
            for par in parameter_list:
                print("Press " + str(parameter_list.index(par) + 1) + " to select " + par + ".")
            choice = int(input(""))
            if choice in range(1, (len(parameter_list) + 1)):
                return parameter_list[choice - 1]
        except ValueError:
            wrong_input()


# def set_start_inventory(player_class):
#     return available_classes[player_class]['starting_inv']


def set_skills(total_points, skill_min, skill_max, skill_list, skillset_name):  # setting up skills one by one
    input("Minimum of 0 and a maximum of " + str(skill_max - 1) + " can be devoted to a skill.\n")
    input("It is recommended to set at least one skill to 5 and one to 1. Press ENTER.\n")
    total = total_points
    skills = {}
    for skl in skill_list:
        skills[skl] = skill_min
        total -= skill_min
    for skl in skill_list:
        skill_value = 0
        while True:
            try:
                print("You got " + str(total) + " points left.")
                answer = int(input("\nAssign points to " + str(skl) + ".\n"))
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
        skills[skl] += skill_value
    if total > 0:
        print("\nYOU HAVE UNUSED POINTS!!! YOU MIGHT HAVE CREATED A LAME CHARACTER!!!\n")
    while True:
        for key in skills.keys():
            print(key + " : " + str(skills[key]))
        answer = (input("\nPress Y to proceed and N to re-set.\n")).lower()
        if answer == "y":
            return skills
        elif answer == "n":
            set_skills(total_points, skill_min, skill_max, skill_list, skillset_name)
            break
        else:
            wrong_input()
