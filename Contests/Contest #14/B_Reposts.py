from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    to, pos, fro = input().split(" ")
    graph[fro.lower()].append(to.lower())

queue = deque(["polycarp"])
visited = set(["polycarp"])
ans = 0

while queue:
    ans += 1
    size = len(queue)

    for _ in range(size):
        ele = queue.popleft()

        if graph[ele]:
            for child in graph[ele]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

print(ans)