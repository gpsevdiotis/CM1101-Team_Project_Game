# maze_"n" where n is any integer is a juction


living_room = {

    "name": "The Living Room",

    "exits": {"east": "The Maze"}

}


maze = {

    "name" : "The Maze",

    "exits": {"east": "maze_1", "west": "The Living Room"}
}
maze_1 = {

    "name" : "maze_1",

    "exits": {"west": "The Maze", "north": "maze_2"}
}

maze_2 = {
    "name" : "maze_2",
    "exits": {"south": "maze_1", "west": "maze_3"}

}

maze_3 = {

    "name" : "maze_3",
    "exits": {"east": "maze_2", "north": "maze_4"}
}

maze_4 = {
    "name" : "maze_4",
    "exits": {"east": "maze_5", "south": "maze_3", "north": "maze_15"}
}

maze_5 = {
    "name" : "maze_5",
    "exits": {"south": "maze_6", "west": "maze_4"}
}

maze_6 = {
    "name" : "maze_6",
    "exits": {"east": "maze_7", "north": "maze_5"}
}


maze_7 = {
    "name" : "maze_7",
    "exits": {"south": "maze_8", "west": "maze_6"}
}

maze_8 = {
    "name" : "maze_8",
    "exits": {"east": "maze_9", "north": "maze_7"}
}
maze_9 = {
    "name": "maze_9",
    "exits": {"north": "maze_10", "west": "maze_8", "east": "maze_dead_end_1"}
}
maze_10 = {
    "name" :"maze_10",
    "exits": {"east": "maze_11", "south": "maze_9"}
}
maze_11 = {
    "name" : "maze_11",
    "exits": {"south": "maze_12", "west": "maze_10"}
}
maze_12 = {
    "name" : "maze_12",
    "exits": {"east": "maze_13", "north": "maze_11"}
}
maze_13 = {
    "name" : "maze_13",
    "exits": {"north": "maze_14", "west": "maze_12"}
}
maze_14 = {
    "name" : "maze_14",
    "exits": {"east": "maze_exit", "south": "maze_13", "west": "maze_26"}
}
maze_15 = {
    "name" : "maze_15",
    "exits": {"east": "maze_16", "south": "maze_4"}
}
maze_16 = {
    "name" : "maze_16",
    "exits": {"north": "maze_17", "west": "maze_15"}
}
maze_17 = {
    "name" : "maze_17",
    "exits": {"west": "maze_18", "south": "maze_16"}
}
maze_18 = {
    "name" : "maze_18",
    "exits": {"north": "maze_19", "east": "maze_17"}
}
maze_19 = {
    "name" : "maze_19",
    "exits": {"east": "maze_20", "south": " maze_18"}
}
maze_20 = {
    "name" : "maze_20",
    "exits": {"east": "maze_dead_end_2", "south": "maze_21", "west": "maze_19"}
}
maze_21 = {
    "name" : "maze_21",
    "exits": {"west": "maze_22", "north": "maze_20"}
}
maze_22 = {
    "name" : "maze_22",
    "exits": {"south": "maze_23", "east": "maze_21"}
}
maze_23 = {
    "name" : "maze_23",
    "exits": {"south": "maze_24", "west": "maze_dead_end_3", "north": "maze_22"}
}
maze_24 = {
    "name" : "maze_24",
    "exits": {"east": "maze_25", "north": "maze_23"}
}
maze_25 = {
    "name" : "maze_25",
    "exits": {"north": "maze_dead_end_4", "west": "maze_24"}
}
maze_26 = {
    "name" : "maze_26",
    "exits": {"north": "maze_27", "east": "maze_14"}
}
maze_27 = {
    "name" : "maze_27",
    "exits": {"east": "maze_28", "south": "maze_26"}
}
maze_28 = {
"name" : "maze_28",
    "exits": {"north": "maze_29", "west": "maze_27"}
}
maze_29 = {
    "name" : "maze_29",
    "exits": {"west": "maze_30", "south": "maze_28"}
}
maze_30 = {
    "name" : "maze_30",
    "exits": {"east": "maze_29", "north": "maze_31"}
}
maze_31 = {
    "name" : "maze _31",
    "exits": {"east": "maze_dead_end_5", "south": "maze_30"}
}
maze_dead_end_1 = {
    "name" : "maze_dead_end_1",
    "exits": {"west": "maze_9"}
}

maze_dead_end_2 = {
    "name" : "maze_dead_end_2",
    "exits": {"west": "maze_20"}
}

maze_dead_end_3 = {
    "name" :"maze_dead_end_3",
    "exits": {"east": "maze_23"}
}

maze_dead_end_4 = {
    "name" :"maze_dead_end_4",
    "exits": {"south": "maze_25"}
}

maze_dead_end_5 = {
    "name" :"maze_dead_end_5",
    "exits": {"west": "maze_31"}
}

maze_exit = {
    "name" : "maze_exit",
    "exits" : {"west": "maze_14"}
}

maze_junctions = {
    "The Living Room": living_room,
    "The Maze": maze,
    "maze_1": maze_1,
    "maze_2": maze_2,
    "maze_3": maze_3,
    "maze_4": maze_4,
    "maze_5": maze_5,
    "maze_6": maze_6,
    "maze_7": maze_7,
    "maze_8": maze_8,
    "maze_9": maze_9,
    "maze_10": maze_10,
    "maze_11": maze_11,
    "maze_12": maze_12,
    "maze_13": maze_13,
    "maze_14": maze_14,
    "maze_15": maze_15,
    "maze_16": maze_16,
    "maze_17": maze_17,
    "maze_18": maze_18,
    "maze_19": maze_19,
    "maze_20": maze_20,
    "maze_21": maze_21,
    "maze_22": maze_22,
    "maze_23": maze_23,
    "maze_24": maze_24,
    "maze_25": maze_25,
    "maze_26": maze_26,
    "maze_27": maze_27,
    "maze_28": maze_28,
    "maze_29": maze_29,
    "maze_30": maze_30,
    "maze_31": maze_31,
    "maze_dead_end_1": maze_dead_end_1,
    "maze_dead_end_2": maze_dead_end_2,
    "maze_dead_end_3": maze_dead_end_3,
    "maze_dead_end_4": maze_dead_end_4,
    "maze_dead_end_5": maze_dead_end_5,
    "maze_exit": maze_exit

}

maze_dead_ends = {
    "maze_dead_end_1": maze_dead_end_1,
    "maze_dead_end_2": maze_dead_end_2,
    "maze_dead_end_3": maze_dead_end_3,
    "maze_dead_end_4": maze_dead_end_4,
    "maze_dead_end_5": maze_dead_end_5,
}
