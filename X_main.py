import X_char_creator
import X_gen_mechanics
import X_object_data


class Player:

    def __init__(self, sexes_list, races_list, starting_position):
        self.name = "Unknown"
        self.sex = X_char_creator.set_parameter_from_list('sex', sexes_list)
        self.race = X_char_creator.set_parameter_from_list('race', races_list)
        self.inventory = {}
        self.position = X_gen_mechanics.starting_position
        self.skills = X_char_creator.set_skills(12, 1, 5, X_char_creator.available_skills, "Skills")
        self.crafting_recipes = []


player1 = Player(X_char_creator.available_sexes, X_char_creator.available_races, X_gen_mechanics.starting_position)


# ____________________________________________CONTAINER CLASSES________________________________________________________
# this class is used for creating all sorts of containers - both item containers like boxes, crates etc. and data
# containers like terminals, computers and so on.
class Container:

    def __init__(self, name, intro_o, intro_l, lock_s, skill, skill_lvl, skill_msg, contents_dict):
        self.name = name
        self.intro_open = intro_o
        self.intro_locked = intro_l
        self.lock_status = lock_s
        self.skill_used_to_open = skill
        self.skill_lvl_required = skill_lvl
        self.skill_open_message = skill_msg
        self.contents = contents_dict


# _______________________________________ITEM CONTAINER SUBCLASS________________________________________________________
# this sub-class is used to create physical item containers
class ItemContainer(Container):

    def __init__(self, name, intro_o, intro_l, lock_s, skill, skill_lvl, skill_msg, contents_dict, item, item_msg):
        super().__init__(name, intro_o, intro_l, lock_s, skill, skill_lvl, skill_msg, contents_dict)
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
                if selected_item in player1.inventory:
                    self.contents[selected_item] -= 1
                    player1.inventory[selected_item] += 1
                else:
                    self.contents[selected_item] -= 1
                    player1.inventory[selected_item] = 1
            elif choice == 'a':
                for item in self.contents:
                    if item in player1.inventory:
                        player1.inventory[item] += self.contents[item]
                        self.contents[item] = 0
                    else:
                        player1.inventory[item] = self.contents[item]
                        self.contents[item] = 0
                break
            elif choice == 'e':
                break
            else:
                X_gen_mechanics.wrong_input()

    def interaction(self):
        """
        function used dor the initial interaction with the container, encompasses the process of opening it either with
        a skill or with an object assigned (like a key etc.)

        """
        print("This is a " + self.name + ".\n")
        if self.lock_status == 1:
            while True:
                print(self.intro_locked)
                if self.skill_used_to_open in player1.skills and \
                        player1.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                    print("Press 'S' to use your " + self.skill_used_to_open + " skills to open this container.")
                elif self.item_used_to_open in player1.inventory:
                    print("Press 'I' to use  " + self.item_used_to_open + " to open this container.")
                choice = (input("Press '0' to exit.\n"))
                try:
                    if choice == 's' and player1.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                        input(self.skill_open_message + "\n")
                        self.lock_status = 0
                        input("The contents are:\n")
                        X_gen_mechanics.list_contents(self.contents)
                        self.item_container_retrieving_items()
                        break
                    elif choice == 'i' and self.item_used_to_open in player1.inventory:
                        input(self.item_open_message + "\n")
                        self.lock_status = 0
                        input("The contents are:\n")
                        X_gen_mechanics.list_contents(self.contents)
                        self.item_container_retrieving_items()
                        break
                    elif choice == '0':
                        break
                except ValueError:
                    X_gen_mechanics.wrong_input()
        elif self.lock_status == 0:
            print(self.intro_open)
            input("The contents are:\n")
            X_gen_mechanics.list_contents(self.contents)
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
                X_gen_mechanics.wrong_input()

    def interaction(self):
        """
        function used dor the initial interaction with the container, encompasses the process of opening it with
        a skill. Most logical skill is hacking but left that as input in the __init__ as may vary from game to game.

        """
        print("This is a " + self.name + ".\n")
        if self.lock_status == 1:
            while True:
                print(self.intro_locked)
                if self.skill_used_to_open in player1.skills and \
                        player1.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                    print("Press 'S' to use your " + self.skill_used_to_open + " skills to hack this terminal.")
                else:
                    X_gen_mechanics.insufficient_skill()
                    break
                choice = (input("Press '0' to exit.\n"))
                try:
                    if choice == 's' and player1.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                        input(self.skill_open_message + "\n")
                        self.lock_status = 0
                        self.data_container_retrieving_data()
                        break
                    elif choice == '0':
                        break
                except ValueError:
                    X_gen_mechanics.wrong_input()
        elif self.lock_status == 0:
            print(self.intro_open)
            self.data_container_retrieving_data()


# ________________________________________________CRAFTING STATION CLASS________________________________________________
# class used to create crafting stations - objects that the player can interact with to use items in their inventory to
# create other items.
class CraftingStation:

    def __init__(self, name, power_st, power_source, intro_pow_up, intro_pow_down, skill, skill_lvl, craf_rec_allowed):
        self.name = name
        self.power_status = power_st
        self.power_source = power_source
        self.intro_powered_up = intro_pow_up
        self.intro_powered_down = intro_pow_down
        self.skill_used_to_operate = skill
        self.skill_lvl_required = skill_lvl
        self.crafting_recipes_allowed = craf_rec_allowed

    def craftstation_power_up(self):
        """
        This function serves to accomodate the added layer of difficulty - the possibility that the craftstation is
        powered down. It allows the player to use a pre-defined (__init__) item to power the craftstation up.

        """
        if self.power_status == 0:
            input(self.intro_powered_down + "\n")
            while True:
                if self.power_source in player1.inventory:
                    print("Press 'I' to use " + self.power_source + ".")
                else:
                    print("You don\'t have the necessary power source in your inventory.\n")
                choice = (input("Press 'E' to exit.\n")).lower()
                if choice == 'i' and self.power_source in player1.inventory:
                    self.power_status = 1
                    player1.inventory[self.power_source] -= 1
                    input(self.intro_powered_up)
                    break
                elif choice == 'e':
                    break
                else:
                    X_gen_mechanics.wrong_input()
        else:
            return self.intro_powered_up + "\n"

    def craftstation_crafting(self):
        """
        This function enables the player to add items from their inventory into the crafting pool and when they think
        they are done, they can attempt crafting which effectively compares the crafting pool to the recipe in the
        recipes dict and depending on whether they are the same or not, gives the player the crafted item or informs
        them that the crafting failed.
        """
        items_used = {}
        input("Select a known crafting recipe:\n")
        known_recipes = player1.crafting_recipes
        if len(known_recipes) != 0:
            for recipe in known_recipes:
                if recipe in self.crafting_recipes_allowed:
                    print("Press " + str(known_recipes.index(recipe) + 1) + " to craft " + recipe)
        else:
            input("You don\'t know any usable recipes.")
            return
        choice = int(input(""))
        selected_recipe = known_recipes[(choice - 1)]
        while True:
            available_items = player1.inventory
            for item in list(available_items.keys()):
                print("Press " + str(list(available_items.keys()).index(item) + 1) + " to add 1x " + item)
            try:
                selection = (input("Press 'C' to craft, press 'E' to exit.\n")).lower()
                if selection.isdigit() is True and int(selection) != 0:
                    selected_item = str(list(available_items.keys())[int(selection) - 1])
                    if selected_item not in items_used:
                        player1.inventory[selected_item] -= 1
                        items_used[selected_item] = 1
                    else:
                        player1.inventory[selected_item] -= 1
                        items_used[selected_item] += 1
                    continue
                elif selection == 'c':
                    if items_used == self.crafting_recipes_allowed[selected_recipe]:
                        if selected_recipe not in player1.inventory:
                            player1.inventory[selected_recipe] = 1
                        else:
                            player1.inventory[selected_recipe] += 1
                        input("You crafted a " + selected_recipe + ".\n")
                        break
                    else:
                        for item in list(items_used.keys()):
                            player1.inventory[item] += items_used[item]
                        input("You failed to craft a " + selected_recipe + ".\n")
                        break
                else:
                    X_gen_mechanics.wrong_input()
            except Error:
                X_gen_mechanics.wrong_input()

    def interaction(self):
        """
        This is the opening function for interacting with a crafting station. Encompasses functions responsible for
        powering up and crafting
        :return:
        """
        print("This is a " + self.name + ".\n")
        self.craftstation_power_up()
        if self.power_status == 0:
            return
        else:
            if self.skill_used_to_operate in player1.skills and \
                    player1.skills[self.skill_used_to_operate] >= self.skill_lvl_required:
                self.craftstation_crafting()
            else:
                X_gen_mechanics.insufficient_skill()


# ________________________________________________ROOM CLASS___________________________________________________________
# this class is used for creating rooms
class Room:

    def __init__(self, level_map, coordinates):
        self.name = level_map[coordinates]["name"]
        self.intro = level_map[coordinates]["intro"]
        self.contents = level_map[coordinates]["contents"]

    def interaction(self):
        print("This place looks like " + self.name + "\n")
        print(self.intro)
        while True:
            for object in self.contents:
                print("Press " + str(list(self.contents.index(object) + 1) + " to interact with " + object.name + "."))
            choice = (input("Press 'I' to view inventory\nPress 'E' to exit.\n")).lower()
            if choice.isdigit() is True and int(choice) in range(1, (len(self.contents)) + 1):
                selection = int(choice)
                self.contents.index(selection).interaction()
            elif choice == 'e':
                X_gen_mechanics.relocate()
            elif choice == 'i':
                for item in player1.inventory.keys():
                    print(item + " x " + player1.inventory[item])
            else:
                X_gen_mechanics.wrong_input()
