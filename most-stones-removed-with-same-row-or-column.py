class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {i: [i, 0] for i in range(len(stones))}

        def finder(x):
            while x != rep[x][0]:
                x = rep[x][0]
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst][1] < rep[snd][1]:
                    rep[fst][0] = snd
                    rep[snd][1] += 1 + rep[fst][1]
                else:
                    rep[snd][0] = fst
                    rep[fst][1] += 1 + rep[snd][1]
            
           
        for i in range(len(stones)):
            for j in range(i, len(stones)):
                ux, uy = stones[i]
                vx, vy = stones[j]

                if ux == vx or uy == vy:
                    union(i, j)

        ans = 0

        for ele in rep:
            if ele == rep[ele][0]:
                ans += rep[ele][1]
        
        return ans