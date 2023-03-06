tc = int(input())
for _ in range(tc):
    w, e, f = map(int, input().split())
    total = 0
    if e <= w:
        if f != 0:
            if 2 * f * e <= f * w:
                total = e * (f + 4)
            else:
                total = w * f + (4 - f) * e
        else:
            total = e * 4
    else:
        total = 4 * w
        
    print(total)