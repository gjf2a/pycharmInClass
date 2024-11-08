from typing import List


def print_sale_list(sales: List[int]):
    for i in range(len(sales)):
        print(f"Sale {i+1}: {sales[i]}")


def main():
    sales = []
    done = False
    while not done:
        print_instructions()

        choice = input("Enter choice: ")
        if choice == '5':
            done = True
        elif choice == '1':
            get_new_sale(sales)
        elif choice == '2':
            print(f"You have sold {len(sales)} items today.")
        elif choice == '3':
            print(f"Total revenue: {get_total(sales)}")
        elif choice == '4':
            print_sale_list(sales)
        else:
            print(f"I don't recognize your selection: {choice}")


def get_total(nums: List[int]) -> int:
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total

def get_total_2(nums: List[int]) -> int:
    total = 0
    for i in range(0, len(nums), 1):
        total += nums[i]
    return total


def get_new_sale(sales: List[int]):
    sale = input("Enter sale amount (in cents): ")
    if not sale.isdigit():
        print(f"That's not a number: {sale}")
    else:
        sales.append(int(sale))


def print_instructions():
    print("Options: ")
    print("1: Enter a sale")
    print("2: See number of sales for the day")
    print("3: See total for the day")
    print("4: See a list of all sales")
    print("5: Quit")


main()