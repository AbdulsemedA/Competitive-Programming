def small(lists, n) -> str:
    lists.sort()
    for ele in range(n - 1):
        if abs(lists[ele+1] - lists[ele]) > 1:
            return "NO"
    return "YES"
    
inputs = int(input())
for _ in range(inputs):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    print(small(nums, n))
