class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)
        queue = deque([0])

        while queue:
            size = len(queue)

            for _ in range(size):
                ele = queue.popleft()
                visited.add(ele)
                
                for child in rooms[ele]:
                    if child not in visited:
                        queue.append(child)
        
        return len(visited) == n