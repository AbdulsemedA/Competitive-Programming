s1 = input()
s2 = input()

total = len(s1) + len(s2)
r1 = len(s1) - 1
r2 = len(s2) - 1

while r1 >= 0 and r2 >= 0:
    if s1[r1] == s2[r2]:
        total -= 2
        r1 -= 1
        r2 -= 1
    else:
        break

print(total)