class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans, queue = [], []
        n = len(tasks)
        tasks = [(i[0], i[1], idx) for idx, i in enumerate(tasks)]
        tasks.sort()
        curr = idx = 0

        while queue or idx < n:
            if not queue and curr < tasks[idx][0]:
                curr = tasks[idx][0]

            while idx < n and tasks[idx][0] <= curr:
                heapq.heappush(queue, (tasks[idx][1], tasks[idx][2]))
                idx += 1

            if queue:
                takes, index = heapq.heappop(queue)
                ans.append(index)
                curr += takes
        
        return ans