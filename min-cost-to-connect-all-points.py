class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, ans = [], 0
        rep = {i: [i, 0] for i in range(len(points))}
    
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

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                ux, uy = points[i]
                vx, vy = points[j]
                edges.append([abs(ux - vx) + abs(uy - vy), i, j])
        
        edges.sort()

        for dis, src, des in edges:
            if finder(src) != finder(des):
                union(src, des)
                ans += dis
        
        return ans