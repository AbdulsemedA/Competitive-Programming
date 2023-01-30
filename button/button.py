tc = int(input())
for _ in range(tc):
    arr = list(input())
    arr.append('^')
    # counts = {}
    ans = []
    left = 0
    if len(arr) > 1:
        right = 1
        while left < len(arr):
            if right < len(arr) and arr[left] != arr[right]:
                ans.append(arr[left])
                left += 1
                right += 1
            else:
                left += 2
                right += 2
        
        print(''.join(sorted(set(ans))))
    else:
        print(*arr)
