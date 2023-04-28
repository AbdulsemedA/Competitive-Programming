tc = int(input())

for _ in range(tc):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    total = x * (x + 1) // 2

    for i in range(n):
        if arr[i] <= x:
            total -= arr[i] * 2
            
    print(total)