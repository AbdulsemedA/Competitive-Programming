import math

X = int(input())
a, ftr = 1, 2
b = num = X

while ftr * ftr <= num:
    if not X % ftr:
        temp = X // ftr
        if max(temp, ftr) < max(a, b):
            if math.lcm(temp, ftr) == num:
                a = ftr
                b = temp
    ftr += 1

print(a, b)