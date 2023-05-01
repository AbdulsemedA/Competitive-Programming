class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
        
        def dfs(node):
            visited.add(node)

            if graph[node]:
                curr = 0
                for ele in graph[node]:
                    if ele not in visited:
                        curr += dfs(ele)

                if not node: 
                    return curr

                if curr or hasApple[node]:
                    return curr + 2
                else:
                    return 0

            return 2 if hasApple[node] else 0
        
        return dfs(0) if n > 1 else 0