from Rooms import Room
from Items, import Item, ItemNames
From Constants import N,S,E,W

itemsList: ItemNames = [
    "stove",
    "bag",
    "sword",
    "hamster",
    "chest",
    "desk",
    "jar",
    "mop",
    "weights",
    "gold",
    "sunglasses",
    "egg",
    "book",
    "pencil",
    "feather",
    "key",
    "chocolate",
    "plunger",
    "suitcase",
    "laptop",
    "box",
    "bottle"
]



type Direction = str 
E : Direction = "east"
W : Direction = "west"
N : Direction = "north"
S : Direction = "south"

directions : List[Direction] = [E,W,N,S]

def create_items():

    Key = Item("key", 5, is_key=True)
    Trap = Item("trap", 0, is_trap=True)
    Bottle = Item("bottle", 15)
    Box = Item("box", 35, [Trap], 0, True)
    Chocolate = Item("chocolate", 5)
    Plunger = Item("plunger", 12)
    Laptop = Item("laptop", 25)
    Sword = Item("sword", 15)
    Hamster = Item("hamster", 20)
    Jar = Item("jar", 7)
    Mop = Item("mop", 10)
    Weights = Item("weights", 50)
    Stove = Item("stove", 130, [Trap])
    Gold = Item("gold", 50)
    Sunglasses = Item("sunglasses", 7)
    Egg = Item("egg", 6)
    Book = Item("book", 20)
    Pencil = Item("pencil", 6)
    Feather = Item("feather", 3)
    Bag = Item("bag", 10, [Feather, Egg], 9, True)
    Suitcase = Item("suitcase", 15, [Laptop], 25, True)
    Chest = Item("chest", 75, [Gold, Sunglasses], 57, True)
    Desk = Item("desk", 100, [Book, Pencil, Key], 31, True)

def create_rooms():

    trap = Room("trap", "", is_trap=True)
    entrance = Room("entrance", "You are in the Main Entrance of a school",[Items.Jar, Items.Chest])
    hall = Room("hall", "You are in a Hallway", [Items.Suitcase])
    bathroom = Room("bathroom", "You are in the Bathroom", [Items.Plunger, Items.Box, Items.Bottle ])
    closet = Room("closet", "You are in the Janitor's Closet", [Items.Bag, Items.Mop], {W : entrance})
    gym = Room("gym", "You are in the Gym", [Items.Weights], {N : entrance, E : hall, S :trap}) 
    cafeteria = Room("cafe", "You are in the Cafeteria", [Items.Stove, Items.Chocolate]) 
    classroom = Room("classroom", "You are in a Classroom", [Items.Desk, Items.Sword, Items.Hamster], {N : cafeteria, S : entrance, E :trap})

    entrance.exits = {N:classroom, E:closet, S: gym, W: hall}
    hall.exits = {E :entrance, W:gym, N:bathroom}
    bathroom.exits = {S:hall, W: cafeteria}
    cafeteria.exits = {S:classroom, E, bathroom}

def build_world:
    create_items()
    create_rooms()


