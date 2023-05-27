n, m = map(int, input().split())
arr = list(map(int, input().split()))
rep = {i: [i, 0] for i in range(1, n + 1)}

def finder(x):
    while x != rep[x][0]:
        x = rep[x][0]
    return x

def union(x, y):
    fst = finder(x)
    snd = finder(y)

    if fst != snd:
        if rep[fst][1] <= rep[snd][1]:
            rep[fst][0] = snd
            rep[snd][1] += 1 + rep[fst][1]
        else:
            rep[snd][0] = fst
            rep[fst][1] += 1 + rep[snd][1]

edges = set()

# for i in range(1, n):
#     for j in range(i + 1, n + 1):
#         edges.add((arr[i - 1] + arr[j - 1], i, j))

for _ in range(m):
    u, v, cost = map(int, input().split())
    if cost < arr[u - 1] + arr[v - 1]:
        edges.discard((arr[u - 1] + arr[v - 1], u, v))
        edges.add((cost, u, v))
    
edges = sorted(edges)
ans = 0

for cost, u, v in edges:
    if finder(u) != finder(v):
        union(u, v)
        ans += cost
    
print(ans)