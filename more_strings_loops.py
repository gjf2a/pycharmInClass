def keep_going() -> bool:
    while True:
        yn = input("Do you want to keep going? (yes/no) ")
        yn = yn.lower()
        if yn[0] == 'y':
            return True
        elif yn[0] == 'n':
            return False
        else:
            print("I did not understand your answer. Try again.")


def accept_any_integer() -> int:
    answered = False
    while not answered:
        num = input("Enter an integer: ")
        num = num.strip()
        if num[0] == '-':
            negative = True
            num = num[1:]
        else:
            negative = False
        if num.isdigit():
            num = int(num)
            if negative:
                num = -num
            answered = True
        else:
            print("That was not an integer. Try again.")
    return num


# Indefinite loops.
# Number of loops depends on the user's input.
def accept_any_float() -> float:
    answered = False
    while not answered:
        num = input("Enter a float: ")
        num = num.strip()
        if num[0] == '-':
            negative = True
            num = num[1:]
        else:
            negative = False
        num_decimal_points = num.count('.')
        if num_decimal_points >= 2:
            print("No more than one decimal point, please.")
        elif num_decimal_points == 1:
            decimal_at = num.find('.')
            before = num[:decimal_at]
            after = num[decimal_at + 1:]
            if not before.isdigit() or not after.isdigit():
                print("That, unfortunately, is not a number. Try again.")
            else:
                answered = True
        else:
            if num.isdigit():
                answered = True
            else:
                print("That's not a number. Try again.")
    num = float(num)
    if negative:
        num = -num
    return num


# Definite loop (I know ahead of time how many loops I need.)
def my_counter(s: str, pattern: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] == pattern:
            count += 1
    return count
