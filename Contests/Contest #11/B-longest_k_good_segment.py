n, k = map(int, input().split())
nums = list(map(int, input().split()))

freq = {}
longest = [0, 0]
start = end = 0

for end in range(n):
    freq[nums[end]] = 1 + freq.get(nums[end], 0)
    
    while len(freq) > k:
        freq[nums[start]] -= 1
        if freq[nums[start]] == 0:
            del freq[nums[start]]
        start += 1

    if end - start + 1 > longest[1] - longest[0] + 1:
        longest = [start, end]
        
print(longest[0] + 1, longest[1] + 1)