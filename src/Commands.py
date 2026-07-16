from typing import Dict, Callable
from Player import Player 
from World import directions


command_funcs : Dict [str: Callable] = {
    "look" : look_cmd,
    "drop" : drop_cmd,
    "take": take_cmd,
    "move": move_cmd, 
    "open": open_cmd, 
    "lives": lives_cmd, 
    "quit" : quit_cmd
}


def parse_command(command:str):
    #checks if command is valid, doesnt check if second part of command is valid 

    if not command:
        #TODO invalid 
    split_command = command.split(" ")

    if len(split_command) > 2:
        #TODO invalid command 

    if not split_command[0] in command_funcs:
        #TODO invalid 
    else:
        return split_command

def look_cmd(command : str, player: Player): 

    print(player.location.desc)


    print("You see a", end=" ")
    for it in player.location.item:
        print(it, end=" ")

def move_cmd(command : str, player Player):

    exits = Player.location.exits

    direction = command[1]

    if not direction in directions 
        print(direction, "is not a direction")

    if not direction in exit:
        print("Cannot go", direction)

  

def handle_command(command: str, player : Player):
    command = parse_command(command)
    
    handler = command_funcs[command[0]]
    handler.(command, player)
