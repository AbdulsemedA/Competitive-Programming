from collections import deque, defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    x, y = input().split()
    graph[x].append(y)
    graph[y].append(x)

start_city, dest_city = None, None
for ele in graph:
    if len(graph[ele]) == 1:
        if start_city is None:
            start_city = ele
        else:
            dest_city = ele
            break

visited = set()
visited.add(start_city)
queue = deque([start_city])
path = [start_city]
while queue:
    node = queue.popleft()
    if node == dest_city:
        break
    for ele in graph[node]:
        if ele not in visited:
            visited.add(ele)
            queue.append(ele)
            path.append(ele)
            
path.reverse()
print(*path)
