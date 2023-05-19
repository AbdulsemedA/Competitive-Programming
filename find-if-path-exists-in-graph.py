class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i: [i, 0] for i in range(n)}

        def finder(x):
            while x != rep[x][0]:
                x = rep[x][0]
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst][1] <= rep[snd][1]:
                    rep[fst][0] = snd
                    rep[snd][1] += 1 + rep[fst][1]
                else:
                    rep[snd][0] = fst
                    rep[fst][1] += 1 + rep[snd][1]
            
           
        for src, des in edges:
            union(src, des)
        
        
        return finder(source) == finder(destination)