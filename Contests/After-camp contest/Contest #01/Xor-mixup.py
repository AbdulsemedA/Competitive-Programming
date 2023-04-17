tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    total = arr[0]
    for i in range(1,len(arr)):
        total ^= arr[i]
    
    for i in arr:
        if i == total ^ i:
            print(i)
            break