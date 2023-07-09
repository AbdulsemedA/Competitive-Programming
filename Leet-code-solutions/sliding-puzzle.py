class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board == [[1,2,3],[4,5,0]]: return 0

        zero = (0, 0)
        lvl = 0
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(x, y):
            return 0 <= x < 2 and 0 <= y < 3
        
        for i in range(2):
            for j in range(3):
                if not board[i][j]:
                    zero = (i, j)
                    break
        
        queue = Deque([[board, zero]])
        visited_board = set([tuple(map(tuple, board))])

        while queue:
            size = len(queue)

            for _ in range(size):
                popped, curr = queue.popleft()
                
                if popped == [[1,2,3],[4,5,0]]: return lvl

                for d in direction:
                    x, y = curr[0] + d[0], curr[1] + d[1]

                    if inbound(x, y):
                        new_board = [row[:] for row in popped]
                        new_board[curr[0]][curr[1]], new_board[x][y] = new_board[x][y], new_board[curr[0]][curr[1]]

                        if tuple(map(tuple, new_board)) not in visited_board:
                            queue.append([new_board, (x, y)])
                            visited_board.add(tuple(map(tuple, new_board)))
            
            lvl += 1
                
        return -1