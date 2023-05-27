n = int(input())
nati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))

nati.sort()
ibsa.sort()
ib = na = 0

for i in range(n):
    if nati[na] <= ibsa[i]:
        ib += 1
        na += 1


if ib > n - ib:
    print("YES")
else:
    print("NO")