class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for src, des in dislikes:
            graph[src].append(des)
            graph[des].append(src)
        
        Set_A = set()
        Set_B = set()
        
        def dfs(node, color):
            if not color:
                Set_A.add(node)
            else:
                Set_B.add(node)
            
            for child in graph[node]:
                if (not color and child in Set_A) or (color and child in Set_B):
                    return False
                if child not in Set_A.union(Set_B) and not dfs(child, 1 ^ color):
                    return False
            return True
        
        for i in range(1, n+1):
            if i not in Set_A.union(Set_B) and not dfs(i, 0):
                return False
        
        return True