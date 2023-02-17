n = int(input())
nums = list(map(int,input().split()))

if sum(nums[:n]) == sum(nums[n:]):
    nums.sort()
if sum(nums[:n]) == sum(nums[n:]):
    print(-1)
else:
    print(*nums)
