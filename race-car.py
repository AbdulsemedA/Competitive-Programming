class Solution:
    def racecar(self, target: int) -> int:
        visited = set([(0, 1)])
        queue = deque([(0, 1, 0)])
        
        while queue:
            pos, speed, mini = queue.popleft()
                    
            if pos == target:
                return mini

            new = []
            new.append((pos + speed, speed * 2, mini + 1))
            if speed > 0:
                new.append((pos, -1, mini + 1))
            else:
                new.append((pos, 1, mini + 1))
            
            for ele in new:
                if ele[:2] not in visited:
                    queue.append(ele)
                    visited.add(ele[:2])

        return -1