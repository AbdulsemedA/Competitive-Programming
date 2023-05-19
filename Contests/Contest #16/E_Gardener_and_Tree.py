from collections import defaultdict, deque

tc = int(input())

for _ in range(tc):
    empty = input()
    n, k = map(int, input().split())
    visited = [1] * (n + 1)
    q = deque()

    graph = defaultdict(list)
    degree = defaultdict(int)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    for i in range(1, n + 1):
        if degree[i] == 1:
            q.append(i)
            visited[i] = 0

    while q and k > 0:
        size = len(q)
        k -= 1

        for _ in range(size):
            u = q.popleft()

            for v in graph[u]:
                if visited[v]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        q.append(v)
                        visited[v] = 0

    print(sum(visited) - 1 + len(q)) if len(graph) else print(0)