import GameIO
from World import build_world
from Player import Player

def run():
    GameIO.welcome()
    build_world()
    player = Player()
    while True:
        command = input("Enter command").strip()
        handle_command(command, player)
