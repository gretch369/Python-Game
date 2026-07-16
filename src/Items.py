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
    inside: List[Item] = field(default_factory=list)   
    inside_weight: int = 0
    openable: bool = False
    is_trap: bool = False
    is_key: bool = False 

type ItemNames = List[Items] 
#move type to constants?
itemMap : Dict[str : Item] = {it.name : it for it in itemsList}

