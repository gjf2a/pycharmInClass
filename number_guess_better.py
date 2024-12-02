import random

def play_once():
    target = random.randint(1, 10)
    print("I'm thinking of a number from 1 to 10.")
    guess = int(input("What do you think it is? "))
    if guess == target:
        print("Congratulations!")
    else:
        print(f"Sorry, it was {target}.")


def main():
    again = "y"
    while again[0] == "y":
        play_once()
        again = input("Would you like to play again? ")
    print("See you later...")


if __name__ == '__main__':
    main()