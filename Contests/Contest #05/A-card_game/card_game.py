n = int(input())
arr = list(map(int, input().split(" ")))
left = 0
right = n - 1
wube = 0
henok = 0
turn = True

while left < right:
    if turn and arr[left] >= arr[right]:
        wube += arr[left]
        left += 1
        turn = False
        
    elif turn and arr[left] < arr[right]:
        wube += arr[right]
        right -= 1
        turn = False
        
    if not turn and arr[left] >= arr[right]:
        henok += arr[left]
        left += 1
        turn = True

    elif not turn and arr[left] < arr[right]:
        henok += arr[right]
        right -= 1
        turn = True
if left <= right:
    wube += arr[left]

print(wube,henok)
