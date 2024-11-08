s = "paper"
print(s[:3])

for c in s:
    if c != 'p':
        print(c)

s = "cycle"
n = 0
for c in s:
    if c == 'c':
        n += 1
print(n)

s = "lollipop"
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        print(s[i])