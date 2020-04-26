from X_char_creator import available_sexes, available_races, available_skills, set_parameter_from_list, set_skills


# ____________________________________________PLAYER CREATOR____________________________________________________________
class PlayerCreator:

    def __init__(self, player_obj):
        self.player_object_edited = player_obj

    def create_character(self):
        self.player_object_edited.name = None
        self.player_object_edited.sex = set_parameter_from_list('sex', available_sexes)
        self.player_object_edited.race = set_parameter_from_list('race', available_races)
        self.player_object_edited.skills = set_skills(12, 1, 5, available_skills, "Skills")
        self.player_object_edited.inventory = {}
        self.player_object_edited.crafting_recipes = []
