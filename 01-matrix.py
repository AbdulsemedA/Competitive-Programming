class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        queue = deque()

        def inBound(x, y):
            return 0 <= x < len(mat) and 0 <= y < len(mat[0])
        
        def bfs(queue, dist):
            while queue:
                size = len(queue)
                dist += 1

                for _ in range(size):
                    i, j = queue.popleft()
                    
                    for x, y in moves:
                        nx = i + x
                        ny = j + y

                        if inBound(nx, ny) and (nx, ny) not in visited and mat[nx][ny]:
                            mat[nx][ny] = dist
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    queue.append((i, j))
                    visited.add((i, j))
        
        bfs(queue, 0)
        return mat