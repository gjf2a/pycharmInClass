wage = float(input("Enter your hourly wage: "))
while wage < 0:
    print("You cannot be paid a negative amount of money!")
    wage = float(input("Enter your hourly wage: "))
hours = float(input("Enter the number of hours you worked this week: "))
while hours < 0:
    print("You cannot work a negative number of hours!")
    hours = float(input("Enter the number of hours you worked this week: "))
if hours > 40:
    overtime = hours - 40
    overtime = overtime / 2
    hours = hours + overtime
print(f"You will be paid ${wage * hours:.2f}")