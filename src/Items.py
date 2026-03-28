"""
Item dataclass 
Each item: name, weight, inside (list of item name strings), inside_weight, openable.
"""
from dataclasses import dataclass, field 
from typing import List, Dict



@dataclass
class Item:
    name: str
    weight: int
    inside: List[str] = field(default_factory=list)   
    inside_weight: int = 0
    openable: bool = False

type ItemNames = List[Items] 


Bag = Item("bag", 10, ["feather", "egg"], 9, True)
Bottle = Item("bottle", 15)
Box = Item("box", 35, ["trap"], 0, True)
Chocolate = Item("chocolate", 5)
Plunger = Item("plunger", 12)
Suitcase = Item("suitcase", 15, ["laptop"], 25, True)
Laptop = Item("laptop", 25)
Bag = Item("bag", 10, ["feather", "egg"], 9, True)
Sword = Item("sword", 15)
Hamster = Item("hamster", 20)
Chest = Item("chest", 75, ["gold", "sunglasses"], 57, True)
Desk = Item("desk", 100, ["book", "pencil", "key"], 31, True)
Jar = Item("jar", 7)
Mop = Item("mop", 10)
Weights = Item("weights", 50)
Stove = Item("stove", 130, ["trap"])
Gold = Item("gold", 50)
Sunglasses = Item("sunglasses", 7)
Egg = Item("egg", 6)
Book = Item("book", 20)
Pencil = Item("pencil", 6)
Feather = Item("feather", 3)
Key = Item("key", 5)


itemsList : ItemNames =  [ Stove,
    Bag,
    Sword,
    Hamster,
    Chest,
    Desk,
    Jar,
    Mop,
    Weights,
    Gold,
    Sunglasses,
    Egg,
    Book,
    Pencil,
    Feather,
    Key,
    Chocolate,
    Plunger,
    Suitcase,
    Laptop,
    Box,
    Bottle
]

itemMap : Dict[str : Item] = {it.name : it for it in itemsList}

