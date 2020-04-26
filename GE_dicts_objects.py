import random

# MISCELLANEOUS DATA USED IN GAME -------------------------------------------------------------------------------------

# example list of available skills
skill_list = ["Science", "Hacking", "Electronics", "Fitness"]

# list of possible codes for the security door in hallway1
possible_codes = [555555, 111111, 222222, 333333, 444444, 666666, 999999]

# list of recipes for crafting
ChemLab_crafting_recipes = {
    "Small Explosive Device": ["Bottle of C3H8O3", "Bottle of V-66", "Steel Canister"]
}


# generation of one security code per game
code_this_iteration = None


def gen_code():
    global code_this_iteration
    code = random.choice(possible_codes)
    code_this_iteration = code


gen_code()


# MISC Dictionaries -------------------------------------------------------------------------------------------------

security_notes_list = ["""A note for warden: we need to re-program the microwave array - I've heard reports that the 
janitorial staff prisoners have been for some time now playing a game where instead of inserting the security code of
the day they would try and navigate the array by foot. Apparently one of them has now figured out the movement of the 
array beams and came up with a way to traverse it from the elevator to the hallway door: 
1. step forward,
2. step right,
3. step left,
4. step left,
5. step forward,
6. step back,
7. step forward,
8. step right,
9. step back,
10. step forward.
The movements of the beams need to be further randomized in order to prevent the possibility of anyone slipping
through."""]

messages_list = ["""'Hey, 
we on for squash this Thursday or what?? 
XO, Li'\n""",
                 """'To all employees, 
please note that there have been several reports received by the command post
recently regarding poor adherence to the Global Safety and Hygiene Guidelines amongst the staff
- in particular in the area of physical interactions with the detainees. Please be advised that
severe disciplinary action will be taken against any employee reported commencing bodily contact with
a detainee in the state or near the state of cryogenic metabolic suspension without proper permissions.
With regards,
Warden D.S.Miller'\n""",
                 """'Jo, I told you several times now, will not say it again - you can\'t use """ +
                 str(code_this_iteration) + """ as the code for the security door. I don\'t care how bad your memory is, 
staple it to your goddamn forehead if need be but the code needs to be changed, now.'\n""",
                 """'Hello friend,
I am writing to you as I am currently in dire need of assistance. I am an elite, well off operator of
a small sized solar trading company. I have just been in the middle of a deal of a lifetime - shipping
Deuterium over to my contact on the Fringe, when my entire transport was requisitioned due to a legal
technicality by the authorities of Trafalgar Waypoint! They say they need time to verify but it will cost
me CR 5k to speed the process up and I put all my ready cash into this investment of a lifetime!
I have a once in a lifetime proposition for you - if you wire me CR 5k now I will share with you the 
ample profits of my business venture - say 10%, circa CR 520,000.00?
Yours truly,
John T'\n""",
                 "'Jo, Order ten more bottles of the stabilising agent for Friday'",
                 """'To all employees,
please note that due to the current circumstances related with the V09 outbreak, the annual Table Tennis Tournament
has been put on hold until further notice. Please revert to the news bulletin for further information.
With regards,
Warden D.S.Miller'\n"""

                 ]
# LOCATION Dictionaries ------------------------------------------------------------------------------------------------


locations = {
    "main": {
        "intro": """\nThe first thing you feel is a pounding pain in your skull. As if there was a tiny, spiked worm
trying to wiggle its way out of your pre-frontal cortex. You free yourself from whatever it was that was holding you 
in place until now and open your eyes slowly to a myriad of flickering lights. Your legs give out at first and you fall
painfully onto your knees - feels like you haven\'t used them for a while. You are wet, cold - and if that weren\'t 
enough - you don\'t remember how you got here or who you are, but we\'ll talk about that later. 
You take a look around...\n"""
    },
    "holding_room1": {
        "intro": """\nThis looks like some sort of a dystopian, techno-jail holding cell. Filled with monitors and 
medical displays, some of which seem to provide data on your own physical condition. The floor seems cold, drenched in 
the fluid leaked your cryo chamber - it seems it malfunctioned and awakened you as a preventive measure for you not to 
drown in the purplish sludge all the lucky popsicles like you are immersed in for long-term storage. There is another 
chamber in the room, also, one of the terminals seems to be active. A portable chemical laboratory also seems 
conveniently deployed right next to your chamber...\n"""
    },
    "holding_room2": {
        "intro": """\nAnother holding cell. There is only one cryogenic chamber here though. You also notice a slight
movement of air coming from a ventilation duct on the far wall. You could probably crawl into it if you could somehow 
lift yourself high enough.\n"""
    },
    "hallway1": {
        "intro": """\nA narrow hallway leading to a security door. There's a door with a sign 'CHEM STORAGE' to your
left and a dark corridor likely leading to other cells to your right. The floor is cold on your bare feet - you need to 
find some shoes soon buddy.\n"""
    },
    "storage_room": {
        "intro": """\nThe room is still small and poorly lit. It seems to be some sort of storage containing various
chemical substances. You investigate the labels and quickly come to the conclusion that they are most likely substances 
necessary for a sustained operation of a cryogenic storage chamber. Wow, you\'re pretty good at this, have you ever 
thought of a career in law enforcement? There's also a tall tools closet in this room, probably locked.\n"""
    },
    "hallway2": {
        "intro": """Another hallway. There's a door to the left with a sign that says: 'SECURITY CONTROL' and a door 
straight ahead. The latter has a red warning label that says 'CAUTION - ACTIVE NON-LETHAL MICROWAVE ARRAY ACTIVE'. 
Sounds fun..."""
    },
    "security_room": {
        "intro": """You find yourself in a narrow room with multiple monitors displaying what you think is security
feed from CCTV cameras. Most of them have been turned off for some reason. You can only see feed from what looks like
the room you woke up in and from an unknown corridor. The display with the corridor view is labeled 'the oven'. There is
an active tablet lying next to the security terminal - the latter seems turned on and secured with a password."""
    },
    "microwave_array": {
        "intro": """There it is - an elevator. This might be your way out. There's also another door here with a label:
'WARDEN OFFICE'."""
    }
}


# OBJECT Dictionaries --------------------------------------------------------------------------------------------------


objects = {
    "craftstation": {
        "intro_chemlab": "This is a portable chemical laboratory.",
        "input1": "It seems that the this device is currently off.",                # indicate status of device
        "input2": "It requires some sort of an energy source to work.",             # indicate what's wrong
        "input3": "It\'s fully operational and charged.",                           # indicate that everything ok
        "input4": "You don't have the skills necessary to operate this device.",    # inform skill insufficient
        "input5": "Press ENTER to use: ",                                           # use power source
        "input6": "You don\'t have any usable power source in your inventory."      # inform that now power source
    },
    "terminal": {
        "input1": "This is a standard computer terminal used in offices and dystopian cryo-prisons accross the world.",
        "input2": "It will need to be hacked if you wish to gain access to the data it holds.",
        "input4": "It seems to be in 'sleep mode' and secured with a password.",
        "input5": "Press 'H' to hack the terminal.",
        "input6": "You work your hacking magic and soon the terminal\'s data is yours to browse.",
        "input7": "It\'s unlocked and accessible.",
        "input8": "You lack the necessary skills to hack this terminal."
    },
    "keypad": {
        "input1": "A simple keypad. Enter the security code:",
        "input2": "The door slides open whirring mechanically. You can go through now."
    },
    "security_door": {
        "input1": "Sturdy security door. There is a keypad if one knows the code of course.",
        "input2mech": """You manage to short circuit the opening mechanism and hard-wire the door to open. 
You can go through them now.""",
        "input3expl": """You use the explosive device to blow up the lock on the security door. When the ringing in 
your ears ceases you can move forward, genius.""",
        "input4": "The door is open now, nothing more to do.",
        "input5keycard": """You use the the key card, the door slides open whirring mechanically."""
    },
    "shipping_manifest": {},
    "container": {
        "intro_chemshelf": """This is a metal, storage shelf. It holds multiple bottles of various sizes containing 
a very diverse selection of chemical substances. Some of them even have skulls - spooky...""",
        "intro_tool_closet": "This is a metal closet used for storing various tools.",
        "intro_sturdy_box": "This is a reinforced, sturdy box for storing various items.",
        "intro_secure_box": "This is a reinforced, box for storing dangerous materials.",
        "intro_DeepSleep_chamber_#2": """A chamber similar to the open you just crawled out of. There's someone inside
but you are unsure as to the status of their vitals. Hey, could have been worse - could have been you in there...""",
        "locked": "It is locked.",
        "intro_DeepSleep_chamber_#3": """A chamber similar to the open you just crawled out of. There's noone inside it
but the chamber is powered up.""",
        "open": "It is open and it\'s contents are available to you.",
        "open_electronics": """You manage to short circuit the opening mechanism and hard-wire it to disable the lock. 
The container is open.""",
        "open_strength": "You manage to force the container open with your bare hands, you magnificent beast.",
        "open_keycard": " You use the keycard to open the container.",
        "open_key": "You use the key to open the container."
    },
    "random": {
        "intro_holding1_poster": """This seems to be some kind of poster containing specific instructions as to how to 
handle the chemicals used for cryogenic storage. There is a line in huge red font at the bottom that says: 'DO NOT UNDER
ANY CIRCUMSTANCES MIX VITRINOL 66 WITH GLYCERINE BEFORE STABILIZING AGENT IS ADDED. THE MIX IS VOLATILE AND CAN MAKE
YOUR CANISTER EXPLODE!!!""",
        "intro_vent_generic": """A narrow ventilation shaft right below the ceiling. Available only to the strongest, 
most agile and desperate of explorers. Probably pretty messy too so a strong resistance to mold and Staphylococcus 
can\'t hurt.""",
        "inside_vent1": """You lift yourself up and crawl into the ventilation shaft. The inside is dark, lit only by 
some residual light coming in from other openings. You feel the air move slightly as you wade through a layer of dust
onwards.""",
        "inside_vent2": """You move past several openings not big enough to fit a grown person. You make a couple of 
turns and soldier on through what seems like and unending claustrphobic nightmare. You do however at last reach an
opening which you can open easily and fit through. It leads to another room...""",
        "intro_prisoner_manifest": """It looks like some kind of shipping manifest, it seems to pertain to the detainees
placed in the adjacent holding cells in the last 48 hours: 'Detainee #127E, Name: John Doe, Memory Landscape: Full 
Personal Reset/ Higher Capabilities retained' - then on the second page - 'Detainee #562E, Name: Susan Hopkirk, Memory
Landscape: Full Personal Reset/ Higher Capabilities removed - re-write to be confirmed'. It seems that either whomever
placed you here doesn\'t know your name either or your parents really hated you and named you John Doe. Let\'s go with 
the first option for now though...""",
        "array_intro": """This looks like a complex array of several microwave emitters, constantly moving and showering
different sections of the corridor with microwave radiation. You make an informed guess that stepping into the
crosshairs of an emitter is extremely painful. After watching the array work for a minute or two you come to the
conclusion that the emitters move in a certain pattern and that gaps open periodically in their coverage of the corridor
. Perhaps it is even possible to navigate the corridor successfully on foot and reach the elevator...""",
        "array_failure": """You take a step and immediately feel like you\'ve just stepped into a red hot oven. You 
scream and stumble back to the door. The sensation passes after a couple of seconds."""
    }
}
