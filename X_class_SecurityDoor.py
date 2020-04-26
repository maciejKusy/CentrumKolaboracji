from X_gen_mechanics import wrong_input, skill_check, item_check


# ________________________________________SECURITY DOOR CLASS___________________________________________________________
# this class is used for creating rooms
class SecurityDoor:

    def __init__(self, world_obj, player_obj, name, intro_o, intro_l, lock_s_bool, skill, skill_lvl, skill_msg, item,
                 item_msg, pin_code, locations_opened_list):
        self.world_object = world_obj
        self.player_object = player_obj
        self.name = name
        self.intro_open = intro_o
        self.intro_locked = intro_l
        self.is_locked_bool = lock_s_bool
        self.skill_used_to_open = skill
        self.skill_lvl_required = skill_lvl
        self.skill_open_message = skill_msg
        self.item_used_to_open = item
        self.item_open_message = item_msg
        self.pin_code = pin_code
        self.locations_opened = locations_opened_list

    def enter_pin(self):
        pin = input("Enter pin code to open:\n")
        if pin == str(self.pin_code):
            input("The door opens.\n")
            self.is_locked_bool = False
            for location in self.locations_opened:
                self.world_object.available_coordinates.append(location)
        else:
            input("Nothing happens.")

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
                choice = (input("Press '1' to interact with keypad\nPress '0' to exit.\n")).lower()
                try:
                    if choice == 's' and self.player_object.skills[self.skill_used_to_open] >= self.skill_lvl_required:
                        input(self.skill_open_message + "\n")
                        self.is_locked_bool = False
                        for location in self.locations_opened:
                            self.world_object.available_coordinates.append(direction)
                        break
                    elif choice == 'i' and self.item_used_to_open in self.player_object.inventory:
                        input(self.item_open_message + "\n")
                        self.is_locked_bool = False
                        for location in self.locations_opened:
                            self.world_object.available_coordinates.append(direction)
                        break
                    elif choice == '1':
                        self.enter_pin()
                        break
                    elif choice == '0':
                        break
                except ValueError:
                    wrong_input()
        elif self.is_locked_bool is False:
            input(self.intro_open)
