class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i: [i, 0] for i in range(1, len(edges) + 1)}
        a = b = 0

        def finder(x):
            while x != rep[x][0]:
                x = rep[x][0]
            
            return x
        
        def union(x, y):
            nonlocal a, b
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst][1] <= rep[snd][1]:
                    rep[fst][0] = snd
                    rep[snd][1] += 1 + rep[fst][1]
                else:
                    rep[snd][0] = fst
                    rep[fst][1] += 1 + rep[snd][1]
            else:
                a, b = x, y
            
           
        for src, des in edges:
            union(src, des)
        
        return [a, b]