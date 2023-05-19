class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        answer = [set() for i in range(n)]
        indeg = defaultdict(int)
        queue = deque()

        for src, des in edges:
            graph[src].append(des)
            indeg[des] += 1

        for i in range(n):
            if not indeg[i]:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()

            for ele in graph[curr]:
                indeg[ele] -= 1
                answer[ele] |= answer[curr]
                answer[ele].add(curr)
                
                if not indeg[ele]:
                    queue.append(ele)
        
        for ele in range(n):
            answer[ele] = sorted(answer[ele])
        
        return answer