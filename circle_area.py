import math

radius = float(input("How large is your circle's radius? "))
while radius <= 0:
    print(f"A circle cannot have a radius of {radius}")
    radius = float(input("How large is your circle's radius? "))
area = math.pi * radius**2

print(f"Area: {area:.4f}")