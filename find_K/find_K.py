t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    ans = "NO"
    nums_dict = {}
    
    for item in nums:
        if item - k in nums_dict or item + k in nums_dict:
            ans = "YES"
            break
        nums_dict[item] = 1 + nums_dict.get(item, 0)
        
    print(ans)
