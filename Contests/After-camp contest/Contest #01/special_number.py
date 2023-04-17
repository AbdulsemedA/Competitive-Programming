tc = int(input())
for _ in range(tc):

    n, k = map(int, input().split())

    ans = 0
    index = 0
    while k:
        if k & 1:
            ans += n ** index
        index += 1
        k >>= 1
    print(ans % (10 ** 9 + 7))