tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    valid = True

    for i in range(1, n):
        if abs(arr[i] - arr[i - 1]) > 1:
            valid = False
            break
    
    print('YES' if valid else 'NO')
    