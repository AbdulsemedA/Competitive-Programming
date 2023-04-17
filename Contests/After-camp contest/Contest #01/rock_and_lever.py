tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = {}
    ans = 0
    for i in arr:
        counter[len(bin(i)) - 2] = 1 + counter.get(len(bin(i)) - 2, 0)
        ans += counter[len(bin(i)) - 2] - 1
    print(ans)