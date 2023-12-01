class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1: return 0
        adj = {i: [] for i in range(n)}

        for i, mgr in enumerate(manager):
            if i != headID: adj[mgr].append(i)

        queue = deque([(headID, 0)])
        visited = [False] * n
        visited[headID] = True
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, time + informTime[node]))
                    visited[neighbor] = True

        return max_time