from X_gen_mechanics import wrong_input, list_contents, skill_check, item_check


# ____________________________________________CONTAINER CLASS__________________________________________________________
# this class is used for creating all sorts of containers - both item containers like boxes, crates etc. and data
# containers like terminals, computers and so on.
class Container:

    def __init__(self, player_obj, name, intro_o, intro_l, lock_s_bool, skill, skill_lvl, skill_msg, contents_dict):
        self.player_object = player_obj
        self.name = name
        self.intro_open = intro_o
        self.intro_locked = intro_l
        self.is_locked_bool = lock_s_bool
        self.skill_used_to_open = skill
        self.skill_lvl_required = skill_lvl
        self.skill_open_message = skill_msg
        self.contents = contents_dict


# _______________________________________ITEM CONTAINER SUBCLASS________________________________________________________
# this sub-class is used to create physical item containers
class ItemContainer(Container):

    def __init__(self, player_obj, name, intro_o, intro_l, lock_s_bool, skill, skill_lvl, skill_msg, contents_dict,
                 item, item_msg):
        super().__init__(player_obj, name, intro_o, intro_l, lock_s_bool, skill, skill_lvl, skill_msg, contents_dict)
        self.item_used_to_open = item
        self.item_open_message = item_msg

    def item_container_retrieving_items(self):
        """
        function used for interacting with items in the container and retrieving (adding them to player1 inventory)
        either 1 by 1 or all at the same time. It adjusts values both in player1.inventory and in self.contents.

        """
        while True:
            for item in self.contents:
                if self.contents[item] > 0:
                    print("Press " + str(list(self.contents.keys()).index(item) + 1) + " to take " + item + ".")
                else:
                    pass
            choice = (input("Press 'A' to take all, press 'E' to exit.\n")).lower()
            if choice.isdigit() is True and int(choice) in range(1, (len(list(self.contents.keys())) + 1)):
                selection = int(choice)
                selected_item = list(self.contents.keys())[selection - 1]
                if selected_item in self.player_object.inventory:
                    self.contents[selected_item] -= 1
                    self.player_object.inventory[selected_item] += 1
                else:
                    self.contents[selected_item] -= 1
                    self.player_object.inventory[selected_item] = 1
            elif choice == 'a':
                for item in self.contents:
                    if item in self.player_object.inventory:
                        self.player_object.inventory[item] += self.contents[item]
                        self.contents[item] = 0
                    else:
                        self.player_object.inventory[item] = self.contents[item]
                        self.contents[item] = 0
                break
            elif choice == 'e':
                break
            else:
                wrong_input()

    def interaction(self):
        """
        function used dor the initial interaction with the container, encompasses the process of opening it either with
        a skill or with an object assigned (like a key etc.)

        """
        print("This is a " + self.name + ".\n")
        if self.is_locked_bool is True:
            while True:
                print(self.intro_locked)
                skill_check(self.player_object, self.skill_used_to_open, self.skill_lvl_required)
                item_check(self.player_object, self.item_used_to_open)
                choice = (input("Press '0' to exit.\n"))
                try:
                    if choice == 's' and self.player_object.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                        input(self.skill_open_message + "\n")
                        self.is_locked_bool = False
                        input("The contents are:\n")
                        list_contents(self.contents)
                        self.item_container_retrieving_items()
                        break
                    elif choice == 'i' and self.item_used_to_open in self.player_object.inventory:
                        input(self.item_open_message + "\n")
                        self.is_locked_bool = False
                        input("The contents are:\n")
                        list_contents(self.contents)
                        self.item_container_retrieving_items()
                        break
                    elif choice == '0':
                        break
                except ValueError:
                    wrong_input()
        elif self.is_locked_bool is False:
            print(self.intro_open)
            input("The contents are:\n")
            list_contents(self.contents)
            self.item_container_retrieving_items()


# ___________________________________________DATA CONTAINER SUBCLASS____________________________________________________
# this class is used to create computer terminals that contain lists of data relevant to the game (passwords, clues,
# instructions, recipes etc.)
class DataContainer(Container):

    def data_container_retrieving_data(self):
        """
        this function serves for the interaction of the player with the set of data contained in the terminal. They can
        view the data lines one by one in search of info/clues etc.

        """
        while True:
            for item in self.contents:
                print("Press " + str(list(self.contents.keys()).index(item) + 1) + " to view " + item + ".")
            choice = (input("Press 'E' to exit.\n")).lower()
            if choice.isdigit() is True and int(choice) in range(1, (len(list(self.contents.keys())) + 1)):
                selection = int(choice)
                selected_item = list(self.contents.keys())[selection - 1]
                print(self.contents[selected_item] + "\n")
            elif choice == 'e':
                break
            else:
                wrong_input()

    def interaction(self):
        """
        function used dor the initial interaction with the container, encompasses the process of opening it with
        a skill. Most logical skill is hacking but left that as input in the __init__ as may vary from game to game.

        """
        print("This is a " + self.name + ".\n")
        if self.is_locked_bool is True:
            while True:
                print(self.intro_locked)
                skill_check(self.player_object, self.skill_used_to_open, self.skill_lvl_required)
                choice = (input("Press '0' to exit.\n"))
                try:
                    if choice == 's' and self.player_object.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                        input(self.skill_open_message + "\n")
                        self.is_locked_bool = False
                        self.data_container_retrieving_data()
                        break
                    elif choice == '0':
                        break
                except ValueError:
                    wrong_input()
        elif self.is_locked_bool is False:
            print(self.intro_open)
            self.data_container_retrieving_data()
