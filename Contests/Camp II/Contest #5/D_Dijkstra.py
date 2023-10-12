from collections import defaultdict
from heapq import *
vertex, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

heap = []
heappush(heap, (0, 0))
visited = set()

dist = [(float('inf'), 0)] * vertex
dist[0] = (0, 0)

while heap:
    d, n = heappop(heap)
    
    if n in visited:
        continue
    
    visited.add(n)
    
    for neigh, val in graph[n]:
        distance = d + val
        if distance < dist[neigh][0]:
            dist[neigh] = (distance, n)
            heappush(heap, (distance, neigh))
if dist[vertex - 1][0] == float('inf'):
    print(-1)
else:
    curr = vertex - 1
    ans = []
    while curr:
        ans.append(curr + 1)
        curr = dist[curr][1]
    ans.append(1)
    print(*ans[::-1])