def weight_label(weight: float) -> str:
    if weight < 10000:
        return "safe"
    elif weight < 12000:
        return "cutting it a little close"
    else:
        return "definitely unsafe"

weight = float(input("How many pounds of cargo have been loaded on the plane?"))
print(f"A load of {weight} pounds is {weight_label(weight)}")

w2 = float(input("How about that other plane? "))
print(f"That other plane is {weight_label(weight)}")