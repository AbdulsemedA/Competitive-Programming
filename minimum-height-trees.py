class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        heights = [0] * n

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
            indeg[des] += 1
            indeg[src] += 1
        
        queue = deque()
        
        for ele in indeg:
            if indeg[ele] < 2:
                queue.append(ele)

        ans = None
        if n == 1: return [0]
        while queue:
            size = len(queue)
            temp = []
            
            for _ in range(size):
                curr = queue.popleft()
                temp.append(curr)
                

                for child in graph[curr]:
                    indeg[child] -= 1
                    # heights[child] = max(heights[child], heights[curr] + 1)
                    if indeg[child] == 1:
                        queue.append(child)
            ans = temp
        
        # print(heights)
        return ans