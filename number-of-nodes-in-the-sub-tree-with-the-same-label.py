class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        count = [[0] * 26 for _ in range(n)]

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
        
        def dfs(node, upper):
            nonlocal count

            if graph[node]:
                for ele in graph[node]:
                    if ele == upper: continue
                    dfs(ele, node)
                    for i in range(26):
                        count[node][i] += count[ele][i]

            count[node][ord(labels[node]) - ord("a")] += 1
        
        dfs(0, -1)
        ans = [count[i][ord(labels[i]) - ord('a')] for i in range(n)]
        return ans