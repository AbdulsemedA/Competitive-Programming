from collections import defaultdict, deque

n, m = map(int, input().split())
city = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    src, des = map(int, input().split())
    graph[src].append(des)
    graph[des].append(src)

visited = set()

def bfs(queue, mini):
    while queue:
        size = len(queue)

        for _ in range(size):
            ele = queue.popleft()

            if graph[ele]:
                for chl in graph[ele]:
                    if chl not in visited:
                        queue.append(chl)
                        mini = min(mini, city[chl - 1])
                        visited.add(chl)
    return mini

ans = 0
for i in range(1, len(city) + 1):
    if i not in visited:
        visited.add(i)
        ans += bfs(deque([i]), city[i - 1])
print(ans)
            