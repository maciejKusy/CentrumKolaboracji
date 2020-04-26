from X_gen_mechanics import starting_position
from X_class_Player import Player
from X_class_PlayerCreator import PlayerCreator
from X_class_Container import ItemContainer, DataContainer
from X_class_CraftingStation import CraftingStation
from X_class_Room import Room
from X_class_SecurityDoor import SecurityDoor
from X_class_World import World

# ____________________________________CREATING PLAYER INSTANCE + CHARACTER CREATION_____________________________________
# object containing all the locations available to the player at a given time:
world1 = World([(5, 1), (5, 2), (4, 2), (6, 1)])

# object containing player characteristics like skills or inv:
player1 = Player(starting_position)

# the player creator:
player_creator = PlayerCreator(player1)
player_creator.create_character()

# ____________________________________CREATING OBJECT INSTANCES________________________________________________________

cell_crystal_ball = DataContainer(player1, "crystal ball", "It's open.", None, False, None, None, None,
                                  {"Vision 1": "A woman riding a bicycle", "Vision 2": "A dwarf riding a motorcycle"})
alchemist_shelf = ItemContainer(player1, "shelf", "Dusty old shelf with ingredients", None, False, None, None, None,
                                {"Eye of Newt": 6, "Small Explosive Device": 1}, None, None)
treasure_chest = ItemContainer(player1, "treasure chest", "It's open", "It's locked", True, "Electronics", 4,
                               "You picked the lock!", {"Gold": 1000}, "Chest Key",
                               "You unlocked it using the Chest Key!")
little_box = ItemContainer(player1, "small wooden box", "It's open", None, False, None, None, None, {"Chest Key": 1},
                           None, None)
security_door1 = SecurityDoor(world1, player1, "security door", "It\'s open", "It\'s locked", True, "Electronics", 5,
                              "You pick the lock!", None, None, 111111, [(5, 3), (4, 3), (5, 4), (6, 4), (5, 5)])

# ____________________________________CREATING ROOM INSTANCES___________________________________________________________
cell_no_1 = Room(world1, player1, "Cell#1", "Cold, dark laboratory of a mad scientist.",
                 [alchemist_shelf, treasure_chest])
hallway_no_1 = Room(world1, player1, "Hallway#1", "A dimly lit hallway.", [security_door1])
storage_room = Room(world1, player1, "Storage room", "A dusty old storage room", [cell_crystal_ball])
cell_no_2 = Room(world1, player1, "Cell#2", "Another cell like the first one", [little_box])
hallway_no_2 = Room(world1, player1, "Hallway #2", "A brightly lit hallway", [])
security_room = Room(world1, player1, "Security control room", "Lots of computers and displays and shit", [])
hallway_no_3 = Room(world1, player1, "Hallway#3", "Yet another fucking hallway", [])
wardens_office = Room(world1, player1, "Warden\'s office", "A neatly organized office.", [little_box])
elevator = Room(world1, player1, "Elevator", "Final destination motherfucker.", [cell_crystal_ball])

# ____________________________________MAP AS DICT - coordinates=keys/room instances=values_____________________________
# level map (dict) storing objects assigned to their respective coordinates
level_1 = {
    (5, 1): cell_no_1,
    (5, 2): hallway_no_1,
    (4, 2): storage_room,
    (6, 1): cell_no_2,
    (5, 3): hallway_no_2,
    (4, 3): security_room,
    (5, 4): hallway_no_3,
    (6, 4): wardens_office,
    (5, 5): elevator
}


# ____________________________________MAIN GAME MECHANICS - if coordinate=coord value in map dict______________________
def game(player_obj, level):
    """
    main game function - calls 'interaction' func of room that the player is currently in
    """
    while True:   # a condition for level clearing to be set here
        level[(player_obj.position["x_axis"], player_obj.position["y_axis"])].interaction()


game(player1, level_1)
