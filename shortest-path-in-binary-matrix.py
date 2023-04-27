class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = set([(0,0)])
        queue = deque([(0, 0)])

        def inBound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid)
        
        def bfs(queue, ans, status):
            status = False

            while queue:
                size = len(queue)
                ans += 1

                for _ in range(size):
                    cx, cy = queue.popleft()
                    
                    if cx == cy == len(grid) - 1 and not grid[cx][cy]:
                        ans += 1
                        status = True
                        break

                    for x, y in direction:
                        i = cx + x
                        j = cy + y

                        if inBound(i, j) and not grid[i][j] and (i, j) not in visited:
                            queue.append((i,j))
                            visited.add((i, j))

                if status: break

            return status, ans

        if grid[0][0]: 
            return -1

        st, ans = bfs(queue, -1, False)
        return ans if ans > -1 and st else -1