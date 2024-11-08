name = input("Enter your name: ")
while name == "":
    print("You didn't type anything!")
    name = input("Try again. What is your name? ")
print(f"Good morning, {name}!")