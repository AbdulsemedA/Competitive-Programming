from collections import deque
tc = int(input())

for _ in range(tc):
    n = int(input())
    mat = []
    for _ in range(2):
        inp = [int(i) for i in input()]
        mat.append(inp)
    
    trap = set()
    visited = set([(1,1)])
    direction = [(1,0), (0, 1),(-1, 0), (0, -1), (1,1),(1,-1),(-1,1),(-1,-1)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]:
                trap.add((i+1, j+1))

    def inbound(x, y):
        return 1 <= x < 3 and 1 <= y < n+1

    def bfs(queue, status):
        while queue:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()

                if (i, j) == (2, n):
                    status = True
                    break
                    
                for x, y in direction:
                    nx = i + x
                    ny = j + y

                    if inbound(nx, ny) and (nx, ny) not in visited and (nx, ny) not in trap:
                        queue.append((nx, ny))
                        visited.add((nx,ny))
            if status:
                break
        return status
    
    queue = deque([(1,1)])
    if bfs(queue, False):
        print("YES")
    else:
        print("NO")
                    