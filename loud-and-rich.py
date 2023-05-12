class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = list(range(len(quiet)))
        indeg = defaultdict(int)
        queue = deque()

        for src, des in richer:
            graph[src].append(des)
            indeg[des] += 1
        
        for ele in range(len(quiet)):
            if not indeg[ele]:
                queue.append(ele)
        
        while queue:
            curr = queue.popleft()

            for ele in graph[curr]:
                indeg[ele] -= 1
                if not indeg[ele]:
                    queue.append(ele)
                
                if quiet[answer[curr]] < quiet[answer[ele]]:
                    answer[ele] = answer[curr]
        
        return answer