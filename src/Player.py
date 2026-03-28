from Items import ItemNames 
from Rooms import Room 
from Constants import MAX_WEIGHT

class Player():

    def __init__(self):

        self.inventory_weight : int = 0
        self.location : Room = Room.entrance 
        self.inventory : ItemNames = []
        self.lives :int = 4 

    
    def add_item(self, item: Item) -> bool:

        if sum(item.weight,item.inside_weight, self.inventory_weight) > MAX_WEIGHT:
            return False 
  
        self.inventory.append(item)
        self.inventory_weight +=  sum(item.weight,item.inside_weight)
        return True 

    def remove_item(self, item: Item) -> None:

        self.inventory_weight -= sum(item.weight, item.inside_weight)
        self.inventory.remove(item)

    def hasItem(self, item:Item) -> bool:
        return item in self.inventory


    def check_inventory(self):

        print("Your inventory contains", end=" ")
        for item in self.inventory:
            print(item,end=",")

        
           

   