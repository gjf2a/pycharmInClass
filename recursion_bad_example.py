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
    play_once()
    again = input("Would you like to play again? ")
    if again[0] == "y":
        main()
    else:
        print("See you later...")


if __name__ == '__main__':
    main()