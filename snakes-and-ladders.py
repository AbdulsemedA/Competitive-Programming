class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        combined = []
        
        for i in range(n - 1, -1, -1):
            if not (n - i) % 2:
                combined += board[i][::-1]
                continue
            combined += board[i]
        
        for i in range(target):
            combined[i] = (i + 1, combined[i])
        
        queue = deque([(1, 0)])
        visited = set([1])
        
        while queue:
            pos, move = queue.popleft()
            if pos == target: return move
            
            for i in range(pos + 1, min(pos + 7, target + 1)):
                src, des = combined[i - 1]
                child = des if des > -1 else src
                if child not in visited:
                    visited.add(child)
                    queue.append((child, move + 1))
        
        return -1