from typing import List, Dict

class Character:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def __repr__(self):
        return f"Character(name='{self.name}', location='{self.location}')"


class Location:
    def __init__(self, neighbors: List[str]):
        self.neighbors = neighbors

    def __repr__(self):
        return f"Location(neighbors={self.neighbors})"


class World:
    def __init__(self, locations: Dict[str, Location], starting_location):
        self.locations = locations
        self.starting_location = starting_location

    def __repr__(self):
        return f"World(locations={self.locations}, starting_location='{self.starting_location}')"

    def can_go_to(self, c: Character) -> List[str]:
        return self.locations[c.location].neighbors

def read_world(filename: str) -> World:
    with open(filename) as file_input:
        locations = {}
        starting_location = None
        for line in file_input:
            line = line.strip()
            colon = line.find(':')
            location = line[:colon]
            if starting_location is None:
                starting_location = location
            neighbors = line[colon + 2:].split(', ')
            locations[location] = Location(neighbors)
        return World(locations, starting_location)

def main():
    world = read_world('world1.txt')
    name = input("What is your character's name? ")
    hero = Character(name, world.starting_location)

    done = False
    while not done:
        print(f"{hero.name} is at {hero.location}.")
        print(f"You can go to {world.can_go_to(hero)}")
        cmd = input("Commands: quit, go [location]> ")
        if cmd == 'quit':
            done = True
        elif cmd[:2] == 'go':
            destination = cmd[3:]
            if destination in world.can_go_to(hero):
                hero.location = destination



