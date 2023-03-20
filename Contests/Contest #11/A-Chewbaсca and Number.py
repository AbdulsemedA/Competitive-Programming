inp = input()
num = [int(i) for i in inp]
n = len(num)

for item in range(n):
    if item == 0:
        if num[item] != 9 and num[item] > 4:
            num[item] = 9 - num[item]
    else:
        if num[item] > 4:
            num[item] = 9 - num[item]

if num[0] == 0:
    num.pop(0)
print(''.join([str(item) for item in num]))

