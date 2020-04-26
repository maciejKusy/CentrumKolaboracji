from X_gen_mechanics import wrong_input


# ____________________________________________PLAYER CLASS_____________________________________________________________
class Player:

    def __init__(self, starting_position):
        self.position = starting_position
        self.move_directions_available = []

    def view_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory.keys():
                print(item + " x " + str(self.inventory[item]))
            print("\n")
        else:
            print("Your inventory is empty.\n")


