from collections import defaultdict
import heapq

n, m, k = map(int, input().split())
distances = {i: float('inf') for i in range(n)}
min_dist = {}
graph = defaultdict(list)
visited = set()

for _ in range(m):
    u, v, w = map(int, input().split())
    
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])

heap = [(0, 0)]
distances[0] = 0

while heap:
    dist, node = heapq.heappop(heap)

    if node in visited:
        continue
    
    visited.add(node)

    for v, w in graph[node]:
        distance = dist + w

        if distance < distances[v]:
            distances[v] = distance
            heapq.heappush(heap, (distance, v))
    
ans = 0

for _ in range(k):
    s, y = map(int, input().split())
    if distances[s-1] <= y:
        ans += 1

print(ans)