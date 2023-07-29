tc = int(input())

for _ in range(tc):
    n, s = map(int, input().split())
    verse = list(map(int, input().split()))
    idx = 0
    curr = 0

    for i in range(n):
        if verse[i] > verse[idx]:
            idx = i
        curr += verse[i]
        if curr > s:
            break

    if curr <= s:
        idx = -1
    print(idx + 1)

            