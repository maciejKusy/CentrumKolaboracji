from X_gen_mechanics import wrong_input, insufficient_skill


# ________________________________________________CRAFTING STATION CLASS________________________________________________
# class used to create crafting stations - objects that the player can interact with to use items in their inventory to
# create other items.
class CraftingStation:

    def __init__(self, player_obj, name, power_st_bool, power_source, intro_pow_up, intro_pow_down, skill, skill_lvl,
                 craft_rec_allowed):
        self.player_object = player_obj
        self.name = name
        self.is_powered_up_bool = power_st_bool
        self.power_source = power_source
        self.intro_powered_up = intro_pow_up
        self.intro_powered_down = intro_pow_down
        self.skill_used_to_operate = skill
        self.skill_lvl_required = skill_lvl
        self.crafting_recipes_allowed = craft_rec_allowed

    def craftstation_power_up(self):
        """
        This function serves to accomodate the added layer of difficulty - the possibility that the craftstation is
        powered down. It allows the player to use a pre-defined (__init__) item to power the craftstation up.

        """
        if self.is_powered_up_bool is False:
            input(self.intro_powered_down + "\n")
            while True:
                if self.power_source in self.player_object.inventory:
                    print("Press 'I' to use " + self.power_source + ".")
                else:
                    print("You don\'t have the necessary power source in your inventory.\n")
                choice = (input("Press 'E' to exit.\n")).lower()
                if choice == 'i' and self.power_source in self.player_object.inventory:
                    self.is_powered_up_bool = True
                    self.player_object.inventory[self.power_source] -= 1
                    input(self.intro_powered_up)
                    break
                elif choice == 'e':
                    break
                else:
                    wrong_input()
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
        known_recipes = self.player_object.crafting_recipes
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
            available_items = self.player_object.inventory
            for item in list(available_items.keys()):
                print("Press " + str(list(available_items.keys()).index(item) + 1) + " to add 1x " + item)
            try:
                selection = (input("Press 'C' to craft, press 'E' to exit.\n")).lower()
                if selection.isdigit() is True and int(selection) != 0:
                    selected_item = str(list(available_items.keys())[int(selection) - 1])
                    if selected_item not in items_used:
                        self.player_object.inventory[selected_item] -= 1
                        items_used[selected_item] = 1
                    else:
                        self.player_object.inventory[selected_item] -= 1
                        items_used[selected_item] += 1
                    continue
                elif selection == 'c':
                    if items_used == self.crafting_recipes_allowed[selected_recipe]:
                        if selected_recipe not in self.player_object.inventory:
                            self.player_object.inventory[selected_recipe] = 1
                        else:
                            self.player_object.inventory[selected_recipe] += 1
                        input("You crafted a " + selected_recipe + ".\n")
                        break
                    else:
                        for item in list(items_used.keys()):
                            self.player_object.inventory[item] += items_used[item]
                        input("You failed to craft a " + selected_recipe + ".\n")
                        break
                else:
                    wrong_input()
            except Error:
                wrong_input()

    def interaction(self):
        """
        This is the opening function for interacting with a crafting station. Encompasses functions responsible for
        powering up and crafting
        :return:
        """
        print("This is a " + self.name + ".\n")
        self.craftstation_power_up()
        if self.is_powered_up_bool is False:
            return
        else:
            if self.skill_used_to_operate in self.player_object.skills and \
                    self.player_object.skills[self.skill_used_to_operate] >= self.skill_lvl_required:
                self.craftstation_crafting()
            else:
                insufficient_skill()
