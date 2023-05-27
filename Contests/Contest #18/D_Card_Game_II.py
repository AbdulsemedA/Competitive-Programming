n = int(input())
nati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))

nati.sort()
ibsa.sort()
swaper = 1
swaps = 0
ib = na = 0

while ib < n:
    if nati[na] <= ibsa[ib]:
        na += 1
        ib += 1
    else:
        ib += 2
        swaps += 1

print(swaps)