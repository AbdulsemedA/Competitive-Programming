from collections import defaultdict

n = int(input())
graph = defaultdict(list)
visited = set()

for i in range(n):
    src, des, cost = map(int, input().split())
    graph[src].append((des, 0))
    graph[des].append((src, cost))

def dfs(node, path_cost):
    visited.add(node)

    if node == 1 and len(visited) == n:
        return path_cost

    for ele, cost in graph[node]:
        if ele not in visited and len(visited) < n:
            result = dfs(ele, path_cost + cost)
            if result is not None:
                return result

    visited.remove(node)
    return None
    
mini = float("inf")

for i in graph[1]:
    visited = set()
    result = dfs(i[0], i[1])
    if result is not None:
        mini = min(mini, result)

print(mini)