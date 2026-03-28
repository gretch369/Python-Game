"""
Room classroom 
Represents the different rooms in the game map
"""

from Items import ItemNames, Item
import Items 
from Constants import Direction, N, E, S, W
from typing import List, Tuple
from dataclasses import dataclass


class Room:
    def __init__(self, rname : str, desc : str , items : ItemNames, exits : List[Tuple[Direction, Room]] = []):
        self.rname = rname
        self.desc = desc 
        self.items = items 
        self.exits = exits 

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        self.items.remove(item)

    def hasItem(self, item:Item) -> bool:
        return item in self.items 

    def checkRoom(self):
        print(self.desc)
        print(f"The {self.rname} contains a ", end="")
        for it in self.items:
            print(items, end=",")


type RoomNames = List[Room] 
trap = Room("trap", "", [])
entrance = Room("entrance", "You are in the Main Entrance of a school",[Items.Jar, Items.Chest])
hall = Room("hall", "You are in a Hallway", [Items.Suitcase])
bathroom = Room("bathroom", "You are in the Bathroom", [Items.Plunger, Items.Box, Items.Bottle ])
closet = Room("closet", "You are in the Janitor's Closet", [Items.Bag, Items.Mop], [(W, entrance)])
gym = Room("gym", "You are in the Gym", [Items.Weights], [(N, entrance), (E, hall), (S, trap)]) 
cafeteria = Room("cafe", "You are in the Cafeteria", [Items.Stove, Items.Chocolate]) 
classroom = Room("classroom", "You are in a Classroom", [Items.Desk, Items.Sword, Items.Hamster], [(N, cafeteria), (S, entrance), (E, trap)])


entrance.exits = [(N, classroom), (E, closet), (S, gym), (W, hall)] 
hall.exits = [(E, entrance), (W, gym), (S,trap), (N, bathroom)]
bathroom.exits = [(S, hall), (W, cafeteria)]
cafeteria.exits = [(S, classroom), (E, bathroom)]


roomList : RoomNames = [entrance, hall, bathroom, closet, gym, classroom, cafeteria, trap]