import heapq

n, m = map(int, input().split())
start = list(map(int, input().split()))
ui, vi = start
x, y = map(int, input().split())
maze = []
visited = set()
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def inbound(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    maze.append(list(input()))

ans = 0
queue = [((ui-1, vi-1), 0, 0)]
visited.add((ui-1, vi-1))

while queue:
    node, left, right = heapq.heappop(queue)
    ans += 1
    
    for uc, vc in direction:
        uf, vf = node[0] + uc, node[1] + vc

        if inbound(uf, vf) and maze[uf][vf] != '*' and (uf, vf) not in visited:
            if vc == 1:
                if right + 1 > y:
                    continue
            
            if vc == -1:
                if left + 1 > x:
                    continue

            if node[1] - vf > 0:
                heapq.heappush(queue, ((uf, vf), left + 1, right))
                

            elif node[1] - vf < 0:
                heapq.heappush(queue, ((uf, vf), left, right + 1))
            
            elif not node[1] - vf:
                heapq.heappush(queue, ((uf, vf), left, right))
            
            visited.add((uf, vf))

print(ans)





# # import heapq

# n, m = map(int, input().split())
# start = list(map(int, input().split()))
# ui, vi = start
# x, y = map(int, input().split())
# maze = []
# visited = set()
# direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# def inbound(x, y):
#     return 0 <= x < n and 0 <= y < m

# for i in range(n):
#     maze.append(list(input()))

# # print(maze)

# ans = 0
# queue = [(ui-1, vi-1, 0, 0)]  

# while queue:
#     node_x, node_y, left, right = queue.pop(0)
#     if (node_x, node_y) in visited:
#         continue

#     ans += 1
#     visited.add((node_x, node_y))

#     for uc, vc in direction:
#         uf, vf = node_x + uc, node_y + vc

#         if inbound(uf, vf) and maze[uf][vf] != '*':
#             if vc == 1 and right + 1 <= y:
#                 queue.append((uf, vf, left, right + 1))
#             elif vc == -1 and left + 1 <= x:
#                 queue.append((uf, vf, left + 1, right))
#             elif not vc:
#                 queue.append((uf, vf, left, right))

# print(ans)