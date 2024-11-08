longest_name = ""
stop_now = False
print("Enter a series of names. Enter a blank line to quit.")
while not stop_now:
    name = input("Enter a name: ")
    if len(name) == 0:
        stop_now = True
    elif len(name) >= len(longest_name):
        longest_name = name

print(f"The longest name you entered was {longest_name}.")