# Data types (synonym: "class")
#
# * Scalar types
# integers
# floats
# booleans
#
# * Aggregate types
#   * Things you can use with a for loop
# strings
# lists
# dictionaries
# file handles
# tuples

import random

class Counter:
    def __init__(self):
        self.count = 0

    # Methods
    def increment(self):
        self.count += 1


class Car:
    def __init__(self, fuel_capacity, mpg, fuel_in_tank=None, odometer=0):
        self.fuel_capacity = fuel_capacity
        if fuel_in_tank is None:
            self.fuel_in_tank = fuel_capacity
        else:
            self.fuel_in_tank = fuel_in_tank
        self.mpg = mpg
        self.odometer = odometer

    def __repr__(self):
        return f"Car(fuel_capacity={self.fuel_capacity}, mpg={self.mpg}, fuel_in_tank={self.fuel_in_tank}, odometer={self.odometer})"

    def drive(self, distance: float):
        fuel_consumed = distance / self.mpg
        if fuel_consumed > self.fuel_in_tank:
            fuel_consumed = self.fuel_in_tank
            distance = fuel_consumed * self.mpg
        self.fuel_in_tank -= fuel_consumed
        self.odometer += distance

    def fill_up(self):
        self.fuel_in_tank = self.fuel_capacity


def drive_around():
    mpg = float(input("Enter miles per gallon: "))
    tank = float(input("Enter fuel tank size in gallons: "))
    my_car = Car(tank, mpg)
    done = False
    while not done:
        print(f"{my_car.fuel_in_tank} gallons left")
        print(f"odometer: {my_car.odometer}")
        choice = input("Enter 'd [distance]' to drive, f to refuel, or q to quit: ")
        if choice == 'q':
            done = True
        elif choice == 'f':
            my_car.fill_up()
        elif choice[0] == 'd':
            parts = choice.split()
            distance = float(parts[1])
            my_car.drive(distance)


class RockPaperScissorsPlayer:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def pick_move(self) -> str:
        moves = ['rock', 'paper', 'scissors']
        return random.choice(moves)

    def i_won(self, my_move: str, opponent_move: str) -> bool:
        if my_move == 'rock' and opponent_move == 'scissors' or \
                my_move == 'scissors' and opponent_move == 'paper' or \
                my_move == 'paper' and opponent_move == 'rock':
            return True
        else:
            return False

    def play_round(self, opponent: 'RockPaperScissorsPlayer'):
        my_move = self.pick_move()
        opponent_move = opponent.pick_move()
        print(f"Player 1: {my_move} Player 2: {opponent_move}")
        if self.i_won(my_move, opponent_move):
            self.wins += 1
            opponent.losses += 1
            print("Player 1 wins")
        elif opponent.i_won(opponent_move, my_move):
            opponent.wins += 1
            self.losses += 1
            print("Player 2 wins")
        else:
            self.ties += 1
            opponent.ties += 1
            print("Tie")

def simulation_rps(num_rounds: int):
    p1 = RockPaperScissorsPlayer()
    p2 = RockPaperScissorsPlayer()
    for round in range(num_rounds):
        print(f"Round {round + 1}")
        p1.play_round(p2)
        print(f"Player 1 WLT: {p1.wins} {p1.losses} {p1.ties}")
        print(f"Player 2 WLT: {p2.wins} {p2.losses} {p2.ties}")