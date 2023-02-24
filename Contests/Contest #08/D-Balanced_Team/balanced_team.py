n = int(input())

nums = list(map(int, input().split(" ")))
nums.sort()
# print(nums)
maxi = left = right = 0

while right < n:
    if abs(nums[right] - nums[left]) <= 5:
        right += 1
    else:
        maxi = max(maxi, right - left)
        # print(maxi)
        while abs(nums[right] - nums[left]) > 5:
            left += 1
    
    maxi = max(maxi, right - left)

print(maxi)