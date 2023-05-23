class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        path_exist = [set() for i in range(numCourses)]
        degree = defaultdict(int)
        queue = deque()

        for src, des in prerequisites:
            graph[src].append(des)
            degree[des] += 1
       
        for ele in range(numCourses):
            if not degree[ele]:
                queue.append(ele)
        
        while queue:
            curr = queue.popleft()

            for ele in graph[curr]:
                degree[ele] -= 1

                if not degree[ele]:
                    queue.append(ele)

                path_exist[ele].add(curr)
                path_exist[ele].update(path_exist[curr])
        
        answer = [False] * len(queries)

        for idx, [u, v] in enumerate(queries):
            if u in path_exist[v]:
                answer[idx] = True
        
        return answer