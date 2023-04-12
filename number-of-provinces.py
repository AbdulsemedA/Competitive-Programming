class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        n = len(isConnected)

        def dfs(node):
            visited.add(node)
            
            for child in range(n):
                if isConnected[node][child] and child not in visited:
                    dfs(child)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count