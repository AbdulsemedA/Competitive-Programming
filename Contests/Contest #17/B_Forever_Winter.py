from collections import defaultdict
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    degree = defaultdict(int)
    x = y = 0

    for _ in range(m):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    
    for i in range(1, n + 1):
        if degree[i] == 1:
            y += 1
    
    x = n - y - 1
    print(x, y//x if x else 0)

