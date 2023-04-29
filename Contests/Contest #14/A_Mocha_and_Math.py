tc = int(input())
for _ in range(tc):
    n = int(input())
    array = list(map(int, input().split()))
    size = len(array)
    curr = array[:]

    while size > 1:
        array = curr[:]
        size = len(array)
        curr = []
        left, right = 0, len(array) - 1
        while left <= right:
            curr.append(array[left] & array[right])
            left += 1
            right -= 1
    print(array[0])
