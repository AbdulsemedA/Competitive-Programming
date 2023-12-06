class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {i: i for i in range(len(strs))}
        
        def finder(x):
            while x != rep[x]:
                x = rep[x]
            return x
        
        def union(x, y):
            rep[finder(x)] = finder(y)
        
        def similar(a, b, n):
            i = diff = 0
            while i < n:
                if a[i] != b[i]: diff += 1
                i += 1
            return diff <= 2
        

        for i in range(len(strs)):
            for j in range(len(strs)):
                if similar(strs[i], strs[j], len(strs[i])):
                    union(i, j)
                    
        ans = set()
        for ele in rep:
            if finder(ele) not in ans:
                ans.add(finder(ele))
        
        return len(ans)