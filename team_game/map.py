from items import *
from maze import *

room_master_bedroom = {

    "name": "The Master Bedroom",

    "description": """You've woken up in a strange room and find yourself lying on the cold floor in the corner ofthe room. You notice a lit fireplace
and you feel warm and a sense of hope, you don't understand it but want more of it. In the room you also see a bed, bathroom door,
wardrobe and outside the bedroom door you see the landing leading to some stairs.""",

    "exits":
        {

            "east": "The Bathroom",
            "west": "The Wardrobe",
            "south": "The Landing"

        },

    "visible_items": [item_candle_1, item_fireplace, item_bed],

    "examined": False,

    "examine_items":[item_matchbox],

    "examine_description": """\nYou notice that next to the candle there are some matches that may be useful in future, you also start to feel some
hints of familiarity with this room. Maybe because it's a bedroom and thoes are always welcoming.""",

    "visible": True

}

room_bathroom = {

    "name": "The Bathroom",

    "description":
        """The bathroom looks like one of thoes typicall 19th century ones, all the dark wood and marble. The only difference is that there is a
smear of what seems like blood on the mirror. You decide not to investigate futher but are starting to get worried.""",

    "exits":
        {

            "west": "The Master Bedroom"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nThere is really seems to be nothing more to this room, nontheles, you decide to search the drawers, to no avail.""",

    "visible": True

}

room_wardrobe = {

    "name": "The Wardrobe",

    "description": """You open the wardrobe to see nothing, which is dissapoiting, considering how big this house seems. You would think they had too many
    clothes for their own good.""",

    "exits":
        {

            "east": "The Master Bedroom"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nA slightly more in depth examination you pick up on what seem like scratches made by hangers but nothing else.""",

    "visible": True

}

room_landing = {

    "name": "The Landing",

    "description": "The old wooden stairs creek as you slowly tip toe down the stairs",

    "exits":
        {

            "north": "The Master Bedroom",
            "down": "The Start of the Hallway"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing at all to see here, you leave a bit dissapointed""",

    "visible": True

}

room_hallway_1 = {

    "name": "The Start of the Hallway",

    "description": "You notice a long hallway with a large painting that takes up the entire wall at the end and the kitchen door to your right.",

    "exits":
        {

            "west": "The Centre of the Hallway",
            "north": "The Kitchen",
            "up": "The Landing"

        },

    "visible_items": [item_painting_1],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nYou pick up on a painting on the wall to your right, it depicts a man holding his newborn child. You
seem to recognise both but you look at the baby with more warth than the father.""",

    "visible": True

}

room_hallway_2 = {

    "name": "The Centre of the Hallway",

    "description": """Further walking down the hallway you see the dining room entrance to your left. The painting at the end of the hall,
 is bigger now and you can mace out that it seems like stairs leading down to a lower floor.""",

    "exits":
        {

            "south": "The Dining Room",
            "east": "The Start of the Hallway",
            "west": "The End of the Hallway"

        },

    "visible_items": [item_painting_3],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nAfter taking a closer look, you notice yet another painting. In this one however, you notice that the
father from the first picture is standing with a business partner. Both people look happy as if a big deal just went through, however,
you get a bitter feeling looking at this picture, as if you faintly remember this decision imploding.""",

    "visible": True

}

room_hallway_3 = {

    "name": "The End of the Hallway",

    "description": """You are now next to the large painting, you can now see clearly that it is infact a painting of stairs leading down,
    you wonder what this could mean and think about looking closer.""",

    "exits":
        {

            "down": "The Living Room",
            "east": "The Centre of the Hallway"

        },

    "visible_items": [item_painting_door],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nAfter looking closer, you notice a small keyhole on the side of the door, and try to think if you've seen any keys
    in the house...""",

    "visible": True

}

room_kitchen = {

    "name": "The Kitchen",

    "description": """Wow what kind of kitchen is this? There is a kitchen table, microwave, a shelf, oven and a
                   cooker, large fridge and a sink.""",

    "exits":
        {

            "north": "The Pantry",
            "south": "The Start of the Hallway"

        },

    "visible_items": [item_fruit],

    "examined": False,

    "examine_items":[item_key],

    "examine_description": """\nAfter a more in depth look around, you notice a key in a drawer and think if it may
    be useful to bring it with you.""",

    "visible": True

}

room_pantry = {

    "name": "The Pantry",

    "description":
        """You open the pantry door to see that its mostly empty other than an energy bar to right of you on the nearest shelf.""",

    "exits":
        {

            "south": "The Kitchen"

        },

    "visible_items": [item_energybar, item_cake, item_bread],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nThere seems to be nothing interesting about this room""",

    "visible": True

}

room_dining = {

    "name": "The Dining Room",

    "description":
        """You turn to your left and enter the dining room. Inside the dining room you see a large buffet,
        plates,glasses, napkins and utensils well arranged on the table. Moreover there is a nice warm fireplace with
        a candle on the floor beside it """,

    "exits":
        {

            "north": "The Centre of the Hallway"

        },

    "visible_items": [item_fireplace, item_candle_2],

    "examined": False,

    "examine_items":[item_book],

    "examine_description": """\nUnder some cloths you notice a book that is rarely opened, you wonder what it is
doing in the dining room...""",

    "visible": True

}

room_living = {

    "name": "The Living Room",

    "description":
        "You see a lit fireplace, library and front door.",

    "exits":
        {

            "south": "The Maid's Room",
            "north": "The Library",
            "east": "The Maze",
            "down": "The Basement",
            "up": "The End of the Hallway"

        },

    "visible_items": [item_fireplace, item_candle_3],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nThis room has many intrecate decorations but nothing more.""",

    "visible": False

}

room_library = {

    "name": "The Library",

    "description":
        "You see a library full of books but you notice shelf a book is missing.",

    "exits":
        {

            "south": "The Living Room",
            "east": "The Secret Room"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nYou thib=bk about putting the book in the bookshelf.""",

    "visible": True

}

room_secret = {

    "name": "The Secret Room",

    "description":
        "The room appears dusty and rundown with cobwebs along ceiling. You notice a stairway going up",

    "exits":
        {

            "west": "The Library",
            "up": "The Attic"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing worth of mention here""",

    "visible": False

}

room_attic = {

    "name": "The Attic",

    "description":
        """You find yourself in the attic of the mansion. Here you realise that scratched on the wall there is
    a phone connection drawing. There is also a window gazing outwards but you fail to see anything as it is
    the middle of the night.""",

    "exits":
        {

            "down": "The Secret Room"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing worth of mention here""",

    "visible": True

}

room_maids = {

    "name": "The Maid's Room",

    "description":
        """You see a small bed and wardrobe, and a bathroom.""",

    "exits":
        {

            "north": "The Living Room",
            "west": "The Maid's Bathroom"

        },

    "visible_items": [item_bed, item_dolls],

    "examined": False,

    "examine_items":[item_map],

    "examine_description": """\nWhen you look around this room, you notice that one of the maids had made a map, it looks
like a maze and you're not sure """,

    "visible": False

}

room_maids_bathroom = {

    "name": "The Maid's Bathroom",

    "description":
        """EMPTY""",

    "exits":
        {

            "east": "The Maid's Room"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing worth of mention here""",

    "visible": True

}

room_basement = {

    "name": "The Basement",

    "description":
        """You stumble down the trapdoor and safely land on your feet in a slimy dungeon and your candle is broken in
        half. Now your completely submerged in darkness.""",

    "exits":
        {

            "up": "The Living Room"

        },

    "visible_items": [item_phone],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing worth of mention here""",

    "visible": False

}

maze = {

    "name": "The Maze",

    "description":
        """You step outside in the cold night air and notice a maze entrance.""",

    "exits":
        {

            "west": "The Living Room"

        },

    "visible_items": [],

    "examined": False,

    "examine_items":[],

    "examine_description": """\nNothing worth of mention here""",

    "visible": True

}

rooms = {

    "The Master Bedroom": room_master_bedroom,
    "The Bathroom": room_bathroom,
    "The Wardrobe": room_wardrobe,
    "The Landing": room_landing,
    "The Start of the Hallway": room_hallway_1,
    "The Centre of the Hallway": room_hallway_2,
    "The End of the Hallway": room_hallway_3,
    "The Kitchen": room_kitchen,
    "The Pantry": room_pantry,
    "The Dining Room": room_dining,
    "The Living Room": room_living,
    "The Library": room_library,
    "The Secret Room": room_secret,
    "The Attic": room_attic,
    "The Maid's Room": room_maids,
    "The Maid's Bathroom": room_maids_bathroom,
    "The Basement": room_basement,
    "The Maze": maze

}
