class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = {i: [i, 0] for i in range(n) }
    
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
        
        result = [False] * len(requests)

        for idx, [x, y] in enumerate(requests):
            ux = finder(x)
            uy = finder(y)
            state = 0

            for u, v in restrictions:
                fst = finder(u)
                snd = finder(v)

                if ux == fst and uy == snd or ux == snd and uy == fst:
                    state = 1
                    break

            if not state:
                union(x, y)
                result[idx] = True
        
        return result