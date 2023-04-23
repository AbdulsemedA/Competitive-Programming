from collections import defaultdict
n = int(input())

while n:
    def checker(n, edges):
        graph = defaultdict(list)
        for i in range(edges):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        colors = [-1] * (n + 1)

        def dfs(node, color):
            colors[node] = color

            for child in graph[node]:
                if colors[child] == -1:
                    if not dfs(child, color ^ 1):
                        return False
                elif colors[child] == color:
                    return False
            return True
        
        for i in range(1, n+1):
            if colors[i] == -1 and not dfs(i, 0):
                    return False
            
        return True
    
    edges = int(input())
    if checker(n, edges):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
    n = int(input())
