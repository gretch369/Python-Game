"""
Room classroom 
Represents the different rooms in the game map
"""
from Items import ItemNames, Item
from Constants import Direction
from typing import Dict
from dataclasses import dataclass

class Room:
    def __init__(self, rname : str, desc : str , items : ItemNames, exits : Dict[Direction :  Room] = [], is_trap : bool =False):
        self.rname = rname
        self.desc = desc 
        self.items = items 
        self.exits = exits 
        self.is_trap = is_trap

    def addItem(self, item: Item) -> None:
        self.items.append(item)

    def removeItem(self, item: Item) -> None:
        self.items.remove(item)

    def hasItem(self, item:Item) -> bool:
        return item in self.items 

   
type RoomNames = List[Room] 
roomList : RoomNames = [entrance, hall, bathroom, closet, gym, classroom, cafeteria, trap]