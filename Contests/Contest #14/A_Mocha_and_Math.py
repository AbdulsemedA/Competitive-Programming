tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    size = len(arr)
    curr = arr[:]

    while size > 1:
        arr = curr[:]
        size = len(arr)
        curr = []
        left, right = 0, len(arr) - 1
        while left <= right:
            curr.append(arr[left] & arr[right])
            left += 1
            right -= 1
    print(arr[0])
