n, m, k = map(int, input().split())
arr = []
freinds = 0

for _ in range(m + 1):
    arr.append(int(input()))

for i in range(m):
    if bin(arr[m] ^ arr[i]).count('1') <= k:
        freinds += 1

print(freinds)