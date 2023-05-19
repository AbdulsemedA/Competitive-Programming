class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        graph = defaultdict(list)
        visited = set()

        for src, des in adjacentPairs:
            count[src] += 1
            count[des] += 1
            graph[src].append(des)
            graph[des].append(src)
        
        def dfs(node, num):
            num.append(node)

            for ele in graph[node]:
                if ele not in visited:
                    visited.add(ele)
                    dfs(ele, num)

            return num

        for i in count:
            if count[i] == 1:
                visited.add(i)
                return dfs(i, [])