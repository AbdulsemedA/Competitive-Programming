q = int(input())
for _ in range(q):
    n = int(input())
    status = True

    side = list(map(int, input().split()))
    side.sort()
    val = set()

    l1, l2 = 0,1
    r1, r2 = 4*n - 2, 4*n - 1

    while l2 < r1:
        if side[l1] != side[l2] or side[r1] != side[r2]:
            status = False
            break
        val.add(side[r1] * side[l1])
        l1 += 2
        l2 = l1 + 1
        r2 -= 2
        r1 = r2 - 1
    if status:
        if len(val) != 1:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")