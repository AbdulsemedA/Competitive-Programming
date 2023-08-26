from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))

HMap = defaultdict(int)
counter = 0

for i in range(n):
    if a[i] ^ x in HMap:
        counter += HMap[a[i] ^ x]
    HMap[a[i]] = 1 + HMap.get(a[i], 0)

print(counter)