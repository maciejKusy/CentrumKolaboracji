from X_gen_mechanics import wrong_input


# ________________________________________________WORLD CLASS__________________________________________________________
# this class is used for stating the locations that are open to the player in the game world
# The list will evolve as player opens doors and navigates obstacles etc.
class World:

    def __init__(self, locations_available_on_start_list):
        self.available_coordinates = locations_available_on_start_list
