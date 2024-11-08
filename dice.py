import random

def die_roll():
    roll = random.random()
    if roll < 1/6:
        return 1
    elif roll < 1/3:
        return 2
    elif roll < 1/2:
        return 3
    elif roll < 2/3:
        return 4
    elif roll < 5/6:
        return 5
    else:
        return 6

print(die_roll())
print(die_roll())
print(die_roll())
print(die_roll())
print(die_roll())
print(die_roll())
print(die_roll())
print(die_roll())