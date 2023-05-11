class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        safe = set()

        def path(node):
            if color[node] == 1: return False
            if color[node] == 2: return True
            color[node] = 1

            if graph[node]:
                for child in graph[node]:
                    if color[child] == 1 or not path(child):
                        return False
                
            color[node] = 2
            safe.add(node)
            return True
        
        for i in range(n):
            if not color[i]:
                path(i)
        
        return sorted(safe)