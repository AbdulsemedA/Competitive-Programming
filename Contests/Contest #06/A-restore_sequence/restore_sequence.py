testcase = int(input())
for _ in range(testcase):
    n =int(input())
    nums = list(map(int,input().split()))
    left = 0
    right = n - 1
    res = []
    while left <= right:
        res.append(nums[left])
        left += 1
        if left <= right:
            res.append(nums[right])
            right -= 1
 
    print(*res)
