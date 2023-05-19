class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        graph = defaultdict(list)
        result = []

        for des, src in prerequisites:
            graph[src].append(des)
            indeg[des] += 1
        
        queue = deque([i for i in range(numCourses) if not indeg[i]])
        
        while queue:
            curr = queue.popleft()
            result.append(curr)

            if graph[curr]:
                for ele in graph[curr]:
                    indeg[ele] -= 1
                    if not indeg[ele]:
                        queue.append(ele)
                
        return len(result) == numCourses