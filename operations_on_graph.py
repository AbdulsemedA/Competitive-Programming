from collections import defaultdict
V = int(input())
graph = defaultdict(list)
k = int(input())

for i in range(k):
    command = list(map(int, input().split()))
    if command[0] == 1:
        graph[command[1]].append(command[2])
        graph[command[2]].append(command[1])
    else:
        print(*graph[command[1]])