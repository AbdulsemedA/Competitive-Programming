class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)

        def dfs(i, curr):
            if i == n - 1:
                if curr[-1] == n - 1:
                    paths.append(curr)
                return

            if graph[i]:
                for j in range(len(graph[i])):
                    dfs(graph[i][j], curr + [graph[i][j]])
            return
        
        dfs(0, [0])
        return paths