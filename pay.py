wage = float(input("Enter your hourly wage: "))
hours = float(input("Enter the number of hours you worked this week: "))
if hours > 40:
    overtime = hours - 40
    overtime = overtime / 2
    hours = hours + overtime
print("You will be paid", wage * hours)
print(f"You will be paid ${wage * hours:.2f}")