mean_was_computed = False
while not mean_was_computed:
    number = 0
    total = 0
    count = 0
    while number != "":
        number = input("Enter a number: ")
        if number.isnumeric():
            number = float(number)
            total += number
            count += 1
        elif len(number) > 0:
            print(f"{number} wasn't a number. Try again.")

    if count == 0:
        print("Sorry, I cannot compute a meaningless mean.")
    else:
        print(f"Mean: {total / count}")
        mean_was_computed = True