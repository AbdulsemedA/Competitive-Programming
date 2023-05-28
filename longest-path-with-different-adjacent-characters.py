class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        mapping = defaultdict(list)
        paths_mapping = defaultdict(list)

        for child, par in enumerate(parent):
            if par == -1: continue
            mapping[par].append(child)

        def helper(parent):
            nonlocal maxPath
            res = 0
            
            for neighbour in mapping[parent]:
                path = helper(neighbour)
                
                if s[parent] != s[neighbour]:
                    res = max(res, path + 1)
                    paths_mapping[parent].append(path + 1)
            
            twoPaths = heapq.nlargest(2, paths_mapping[parent])
            maxPath = max(maxPath, sum(twoPaths) + 1)
            return res
        
        maxPath = 0
        helper(0)
        return maxPath