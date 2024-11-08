# "Sentinel loop"
import math

valid_radius = False # sentinel
while not valid_radius:
    radius = float(input("How large is your circle's radius? "))
    if radius <= 0:
        print(f"A circle cannot have a radius of {radius}")
    else:
        valid_radius = True

area = math.pi * radius**2

print(f"Area: {area:.4f}")