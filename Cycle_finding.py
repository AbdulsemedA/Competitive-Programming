from collections import defaultdict, deque
import math
import heapq
 
def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def SI(): return sorted(list(map(int,input().split())))
 
def bellmanFord(graph, src, n):
    distance = [0 for _ in range(n)]
    predeccesor = [float("inf") for _ in range(n)]    
    distance[src] = 0
 
    for i in range(n - 1) :
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predeccesor[v] = u
   
    return [distance, predeccesor]
 
def detecteNegativeCycle(graph, distance, predeccesor,n):
    
    lastPredeccesor = -1
 
    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            lastPredeccesor = v
 
 
    if lastPredeccesor != -1:
        visited = set()
        cycle_path = []
    
        while True:
            if predeccesor[lastPredeccesor] == float("inf"):
                cycle_path.append(1)
                break
            
            cycle_path.append(lastPredeccesor + 1)
 
            if lastPredeccesor in visited:
                break
 
            visited.add(lastPredeccesor)
            lastPredeccesor = predeccesor[lastPredeccesor]
            
    
            
 
        return reversed(cycle_path)
    
    else:
        return False
 
 
def solve():
    n, m = MI()
    graph = []
 
    for _ in range(m):
        u, v, w = MI()
        graph.append([u - 1, v - 1, w])
 
    dis,parents = bellmanFord(graph, 0, n)
 
    res = detecteNegativeCycle(graph, dis,parents, n)
 
    if res:
        print("YES")
        print(*res)
    else:
        print("NO")

solve()