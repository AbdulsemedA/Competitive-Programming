n, k = map(int, input().split())
fence = list(map(int, input().split()))

first = sum(fence[:k])
mini = (first, 1)

for i in range(1, n-k+1):
    first = first - fence[i-1] + fence[i+k-1]
    if first < mini[0]:
        mini = (first, i + 1)
    
print(mini[1])