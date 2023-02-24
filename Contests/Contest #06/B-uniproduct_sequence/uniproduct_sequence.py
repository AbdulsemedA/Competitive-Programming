n = int(input())
nums = list(map(int,input().split()))
nums.sort()
negative, zeros, minimum = 0, 0, 0

for i in range(n):
    if nums[i] < 0:
        negative += 1
    elif nums[i] == 0:
        zeros += 1 

for i in range(n):
    if nums[i] < 0:
        minimum += abs(nums[i]) - 1
    elif nums[i] > 0:
        minimum += nums[i] - 1

if negative % 2 == 1:
    if zeros == 0:
        minimum += 2
    else:
        minimum += 1
        zeros -= 1

minimum += zeros

print(minimum)
