tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(input())
    count = n - 1
    for i in range(1, n-1):
        if arr[i - 1] == arr[i + 1]:
            count -= 1
    
    print(count)