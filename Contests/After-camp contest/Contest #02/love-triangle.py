n = int(input())
nums = list(map(int, input().split()))
status = False
check = set(nums)
for i in range(n):
    if nums[i] - 1 < n and nums[i] - 1 > -1:
        curr = nums[i]
        count = 1
        while count <= 3 and curr != i + 1:
            curr = nums[curr - 1]
            count += 1
        if curr == i + 1 and count == 3:
            status = True

if status:
    print("YES")
else:
    print("NO")