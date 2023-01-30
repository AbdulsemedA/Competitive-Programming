tc = int(input())
for _ in range(tc):
    arr = list(input())
    n = len(arr)
    if n < 3:
        print(0)
    else:
        count = {}
        left = right = 0
        mini = n + 1

        while right < n:
            count[arr[right]] = 1 + count.get(arr[right], 0)
            
            while len(count) == 3 and all(count.values()):
                mini = min(mini,right - left + 1)
                count[arr[left]] -= 1 
                left += 1
                
            right += 1
            
        if len(count) != 3:
            mini = 0
        
        print(mini)
