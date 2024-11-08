has_data = False
stop_now = False
print("Enter as many numbers as you like.")
print("Enter a blank line to stop.")

while not stop_now:
    number = input("Enter a number: ")
    if len(number) == 0:
        stop_now = True
    elif number.isnumeric():
        number = float(number)
        if not has_data or number < minimum:
            minimum = number
            has_data = True
    else:
        print(f"{number} is not a number.")

if has_data:
    print(f"The minimum is {minimum}")
else:
    print(f"You didn't type anything.")