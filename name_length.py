name = input("Enter your name: ")
if len(name) < 5:
    print(f"{name} is really short")
elif len(name) < 8:
    print(f"{name} is medium length")
else:
    print(f"{name} is really long")