class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque()
        n, mini = len(grid), 0

        def inbound(x, y): return 0 <= x < n and 0 <= y < n

        def oneIsland(queue):
            while queue:
                dx, dy = queue.popleft()

                for x, y in direction:
                    ux, uy = dx + x, dy + y

                    if inbound(ux, uy) and grid[ux][uy] and (ux, uy) not in visited:
                        visited.add((ux, uy))
                        queue.append((ux, uy))
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j))
                    oneIsland(queue)
                    break
            else: 
                continue
            break
        
        queue.extend(visited)
        
        while queue:
            size = len(queue)

            for _ in range(size):
                dx, dy = queue.popleft()

                for x, y in direction:
                    ux, uy = dx + x, dy + y

                    if inbound(ux, uy) and (ux, uy) not in visited:
                        if grid[ux][uy]:
                            return mini
                        visited.add((ux, uy))
                        queue.append((ux, uy))
            mini += 1