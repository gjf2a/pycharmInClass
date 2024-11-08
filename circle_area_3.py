import math

valid_radius = False  # sentinel
while not valid_radius:
    radius = input("How large is your circle's radius? ")
    if radius.isnumeric() or '-' in radius:
        radius = float(radius)
        if radius <= 0:
            print(f"A circle cannot have a radius of {radius}")
        else:
            valid_radius = True
    else:
        print(f"{radius} cannot be converted to a number.")

area = math.pi * radius ** 2

print(f"Area: {area:.4f}")