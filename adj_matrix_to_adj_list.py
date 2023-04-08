from collections import defaultdict
V = int(input())
graph = defaultdict(list)
for i in range(V):
    row = list(map(int, input().split()))
    for j in range(V):
        if row[j] == 1:
            graph[i].append(j+1)
    if graph[i]:
        print(len(graph[i]), *graph[i])