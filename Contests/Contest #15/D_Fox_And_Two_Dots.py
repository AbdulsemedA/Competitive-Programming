n, m = map(int, input().split())

grid = []
for _ in range(n):
    row = input()
    grid.append([i for i in row])

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def inbound(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(par, curr):
    i, j = curr
    color = grid[i][j]

    for x, y in moves:
        dx = i + x
        dy = j + y

        if inbound(dx, dy) and (dx, dy) != par and grid[dx][dy] == color:
            if (dx, dy) in visited:
                return True
            visited.add((dx, dy))
            return dfs(curr, (dx, dy))
        
    return False

st = False
visited = set()

for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            visited.add((i, j))
            if dfs(None, (i, j)):
                st = True
        if st: break
    if st: break

print("Yes") if st else print("No") 



