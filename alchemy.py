n = int(input())
nums = list(map(int, input().split()))
left, right = 0, n - 1
edward = alphonse = 0

while left <= right:
    if edward <= alphonse:
        edward += nums[left]
        left += 1
    else:
        alphonse += nums[right]
        right -= 1

print(left, n - left)
