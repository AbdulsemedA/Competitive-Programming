from collections import Counter
tc = int(input())

for _ in range(tc):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    freq = Counter(arr)

    for ele in freq:
        ans += min(freq[ele], c)
    
    print(ans)