from Items import ItemNames 
from Rooms import Room 
from Constants import MAX_WEIGHT

class Player():

    def __init__(self):
        self.inventory_weight : int = 0
        self.location : Room = Room.entrance 
        self.inventory : ItemNames = []
        self.lives :int = 3

    
    def takeItem(self, item: Item) -> None:
        #Item is in room
        if not self.location.hasItem:
            print(f"{self.location.rname} does not have a {item.name}")
            return 
        if sum(item.weight,item.inside_weight, self.inventory_weight) > MAX_WEIGHT:
            print(f"{item.name} cannot fit in backpack. Please drop items in your inventory to make space")
            
        self.inventory.append(item)
        self.inventory_weight +=  sum(item.weight,item.inside_weight)
     
    def dropItem(self, item: Item) -> None:
        #can only drop items inside inventory 
        if not self.hasItem(item):
            print(f"You do not have a {item.name} in your inventory")
        self.inventory_weight -= sum(item.weight, item.inside_weight)
        self.inventory.remove(item)


    def hasItem(self, item: Item) -> bool:
        return item in self.inventory

    def openItem(self, item : Item) -> None:
        #can open an item inside inventory or outside inventroy
        #item must be in room or inventory
        #once open the items is removed and cant be added back to item
        #item with stuff inside is now empty 
        if self.hasItem(item) or self.location.hasItem(item):
            if item.openable:
                if not item.inside:
                    print(f"{item.name} is empty")
                    return 
                print(f"You open the {item.rname}. A ", end="")
                #hamster, egg, bottle 
                added_items=[]
                for it in item.inside:  
                    if it.name == "hamster":    
                        print("hamster scurries out")
                    elif it.name == "bottle" or it.name == "egg":
                        print(f"{it.name} rolls out")
                    else:
                        print(f"{it.name}", end=",")
                    added_items.append(it)
                print("falls out")
                if self.hasItem(item):
                    self.inventory.extend(added_items)
                else:
                    self.location.items.extend(added_items)

                item.inside = []
                    
            else:
                print(f"{item.rname} cannot be opened")
        else:
            print(f"You do not have a {item.name} and it is not in the {self.location.rname}")
             
    def move(self, direction : Direction) -> None:

        for dirs, room  in self.location.exits:
            if direction == dirs:
                if room.name == "trap":
                    print("You fell into a trap. You lost a life")
                    self.loseLife()
                else:
                    self.location = room 
                return 

        print(f"You cannot go {direction}")


    def loseLife(self) -> None:
        self.lives -= 1
        if self.lives == 0
            pass
            #TODO end game

    def checkInventory(self):
        print("Your inventory contains", end=" ")
        for item in self.inventory:
            print(item.rname,end=",")

        
           

   