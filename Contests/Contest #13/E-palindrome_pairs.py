n = int(input())
Count = {}
total = 0

for i in range(n):
    s = input()
    odds = 0
    for j in s:
        odds ^= 1 << (ord(j) - ord('a'))
    
    for j in range(26):
        temp = odds ^ (1 << j)
        if temp in Count:
            total += Count[temp]

    if odds in Count:
        total += Count[odds]
        Count[odds] += 1
    else:
        Count[odds] = 1

print(total)