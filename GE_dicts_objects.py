import random

skill_list = ["Agility", "Strength", "Mechanics", "Hacking", "Science"]

possible_codes = [555555, 111111, 222222, 333333, 444444, 666666, 999999]

code_this_iteration = None


def gen_code():
    global code_this_iteration
    code = random.choice(possible_codes)
    code_this_iteration = code


gen_code()

email_list = ["""'Hey, 
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

locations = {
    "main": {
        "intro": """\nThe first thing you feel is a pounding pain in your skull. As if there was a tiny, spiked worm
trying to wiggle its way out of your pre-frontal cortex. You free yourself from whatever it was that was holding you 
in place until now and open your eyes slowly to a myriad of flickering lights. Your legs give out at first and you fall
painfully onto your knees - feels like you haven\'t used them for a while. You are wet, cold - and if that weren\'t 
enough - you don\'t remember how you got here or who you are, but we\'ll talk about that later. 
You take a look around...\n"""
    },
    "holding_room": {
        "intro": """\nFilled with monitors and medical displays, some of which seem to provide data on your own physical 
condition. The floor seems cold, drenched in the fluid leaked your cryo chamber - it seems it malfunctioned and awakened
you as a preventive measure for you not to drown in the purplish sludge all the lucky popsicles like you are immersed in
for long-term storage. There is another chamber in the room, also, one of the terminals seems to be active...\n"""
    },
    "hallway": {
        "intro": """\nA narrow hallway leading to a security door. Doors on both sides, but the ones on the right seem
to have been welded shut. The floor is cold on your bare feet. The door on the left seems to lead to some sort of 
storage area.\n"""
    },
    "storage_room": {
        "intro": """\nThe room is still small and poorly lit. It seems to be some sort of storage containing various
chemical substances. You investigate the labels and quickly come to the conclusion that they are most likely substances 
necessary for a sustained operation of a cryogenic storage chamber. Wow, you\'re pretty good at this, have you ever 
thought of a career in law enforcement? There's also what seems like a shipping manifest on the small table near the 
door.\n"""
    },
    "hallway_junction": """Another rather """
}




objects = {
    "cryo_chamber": {
        "input1": """\nIt's a standard deep-freezing chamber for long term human storage. The outside glass is a bit
foggy but you are able to wipe the condensed water away with your hand. It appears that there\'s someone inside.
You take a closer look...\n""",
        "input2": """\nThe person inside seems to be a male, about fourty years old. Something about his face seems
eerily familiar. Almost as if you\'ve just dreamt who it was and was now trying to remember that dream. 
The chamber seems operational and you don\'t see any obvious way of opening it.\n"""
    },
    "log_terminal": {
        "input1": """\nThis is a standard computer terminal used in offices and dystopian, cryogenic prisons all over
the world you currently seem to know so little about. Seems to be in 'sleep mode' and secured with a password...\n""",
        "input2": "Using your superior hacking skills you manage to unlock the terminal.",
        "input3": "You try to guess the password a couple of times but fail miserably. You\'re no hacker buddy.\n"
    },
    "keypad": {
        "input1": "A simple keypad. Enter the security code:\n",
        "input2": "\nThe door slides open whirring mechanically. You can go through now.\n"
    },
    "security_door": {
        "input1": "\nSturdy security door. There is a keypad if one knows the code of course...\n",
        "input2": "\nYou slide the door open by sheer, brute force. You can go through them now.\n",
        "input3": """\nYou manage to short circuit the opening mechanism and hard-wire the door to open. 
You can go through them now.\n""",
        "input4": """\nYou quickly mix together several of the chemicals you found in the storage room and
let the ensuing, violent chemical reaction blow up the lock on the security door. When the ringing in your ears ceases
you can go forward genius.\n""",
        "input5": "You don\'t have the necessary materials to rig an explosive charge.\n",
        "input6": "The door is open now, nothing more to do.\n"
    },
    "shipping_manifest": {},
    "volatile_chem": {}
}
