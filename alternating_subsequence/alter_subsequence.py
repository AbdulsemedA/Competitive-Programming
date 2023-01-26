tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    maxi = 0
    total = 0

    for val in arr:
        if val > 0:
            if maxi < 0:
                total += maxi
            maxi = max(maxi, val)
        else:
            if maxi >= 0:
                total += maxi
                maxi = val
            else:
                maxi = max(maxi, val)

    total += maxi
    print(total)
