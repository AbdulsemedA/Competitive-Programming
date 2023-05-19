from collections import defaultdict

n, m = map(int, input().split())
members = {}
graph = defaultdict(list)
maxi = []

for i in range(n):
    members[i] = input()

for j in range(m):
    x, y = map(str, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(2 ** n):
    curr_team = []
    idx = 0
    
    while i:
        if i & 1:
            curr_team.append(members[idx])
        idx += 1
        i >>= 1

    size = len(curr_team)
    flag = 0

    for i in range(size):
        for j in range(i + 1, size):
            if curr_team[j] in graph[curr_team[i]]:
                flag = 1
                break
        if flag:
            break

    if not flag:
        if size > len(maxi):
            maxi = curr_team

print(len(maxi))
maxi.sort()
for i in maxi:
    print(i)

    
