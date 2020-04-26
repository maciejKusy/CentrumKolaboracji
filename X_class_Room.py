from X_gen_mechanics import wrong_input


# ________________________________________________ROOM CLASS___________________________________________________________
# this class is used for creating rooms
class Room:

    def __init__(self, world_obj, player_obj, name, intro, contents):
        self.world_object = world_obj
        self.player_object = player_obj
        self.name = name
        self.intro = intro
        self.contents = contents

    def check_move_options(self, choices):
        """
        function printing the directions of movement out of a room that are available at a given moment
        """
        if ((self.player_object.position["x_axis"] + 1), (self.player_object.position["y_axis"])) \
                in self.world_object.available_coordinates:
            choices.append("e")
            print("Press 'e' to move east")
        if ((self.player_object.position["x_axis"] - 1), (self.player_object.position["y_axis"])) \
                in self.world_object.available_coordinates:
            choices.append("w")
            print("Press 'w' to move west")
        if ((self.player_object.position["x_axis"]), (self.player_object.position["y_axis"] + 1)) \
                in self.world_object.available_coordinates:
            choices.append("n")
            print("Press 'n' to move north")
        if ((self.player_object.position["x_axis"]), (self.player_object.position["y_axis"] - 1)) \
                in self.world_object.available_coordinates:
            choices.append("s")
            print("Press 's' to move south")

    def relocate(self):
        """
        function for re-locating the player character. Checks what coordinates are available for selection and
        provides the player with adequate options form movement

        """
        choices = []
        self.check_move_options(choices)
        while True:
            direction = (input("Select direction:\n")).lower()
            if direction not in choices:
                wrong_input()
                self.check_move_options(choices)
                continue
            elif direction == "n":
                self.player_object.position["y_axis"] += 1
                break
            elif direction == "e":
                self.player_object.position["x_axis"] += 1
                break
            elif direction == "s":
                self.player_object.position["y_axis"] -= 1
                break
            elif direction == "w":
                self.player_object.position["x_axis"] -= 1
                break

    def interaction(self):
        """
        this function enables the player to interact with objects in the room and also to view own inventory

        """
        print("This place looks like " + self.name + "\n")
        print(self.intro + "\n")
        while True:
            for obj in self.contents:
                print("Press " + str(self.contents.index(obj) + 1) + " to interact with " + obj.name + ".")
            choice = (input("Press 'I' to view inventory\nPress 'E' to exit.\n")).lower()
            if choice.isdigit() is True and int(choice) in range(1, (len(self.contents)) + 1):
                selection = int(choice)
                self.contents[selection - 1].interaction()
            elif choice == 'e':
                break
            elif choice == 'i':
                self.player_object.view_inventory()
            else:
                wrong_input()
        self.relocate()
