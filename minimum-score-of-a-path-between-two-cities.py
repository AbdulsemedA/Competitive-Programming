class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i: [i, float("inf")] for i in range(1, n + 1)}

        def finder(x):
            while x != rep[x][0]:
                x = rep[x][0]
            
            return x
        
        def union(x, y, dis):
            fst = finder(x)
            snd = finder(y)

            if dis < min(rep[fst][1], rep[snd][1]):
                rep[fst][1] = rep[snd][1] = dis
                rep[snd] = rep[fst]
            else:
                if rep[fst][1] <= rep[snd][1]:
                    rep[snd] = rep[fst]
                else:
                    rep[fst] = rep[snd]
        
        for src, des, dis in roads:
            union(src, des, dis)
        
        f = rep[finder(1)][1]
        s = rep[finder(n)][1]

        return min(s, f)