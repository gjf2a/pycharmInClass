import random

def is_heads():
    if random.random() < 0.5:
        return True
    else:
        return False

count = 0
heads = 0
tails = 0
while count < 100000:
    if is_heads():
        heads += 1
    else:
        tails += 1
    count += 1

print(f"Heads: {heads}")
print(f"Tails: {tails}")