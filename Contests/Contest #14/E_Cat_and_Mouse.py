from collections import deque

n, m, p = map(int, input().split(" "))
grid = [[str(i) for i in input()] for _ in range(n)]
P = list(map(int, input().split()))
# print(P)
move_bindings = {0: (0, 0),  1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
# print(grid)
def inbound(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    for j in range(m):
        if grid[i][j] == "M":
            mouse = (i, j)
            # print("mouse(B): ", mouse)

for ele in P:
    dx, dy = move_bindings[ele]
    nx = mouse[0] + dx
    ny = mouse[1] + dy

    if inbound(nx, ny) and grid[nx][ny] != "#":
        mouse = (nx, ny)

# print("mouse(AF): ", mouse)

def bfs(queue, visited, cells):
    dis = -1
    while queue:
        size = len(queue)
        dis += 1
        if dis > -1 and dis <= p:
            cells += size
        
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in move_bindings.values():
                nx = x + dx
                ny = y + dy
                if inbound(nx, ny) and grid[nx][ny] != "#" and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    return cells

queue = deque([mouse])
print(bfs(queue, set([mouse]), 0))

