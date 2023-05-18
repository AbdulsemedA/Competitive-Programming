class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {i: i for i in set(s1) | set(s2)}
        
        def finder(x):
            while x != rep[x]:
                x = rep[x]
            
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst] <= rep[snd]:
                    rep[snd] = fst
                else:
                    rep[fst] = snd
        
        ans = []
        for i in range(len(s1)):
            union(s1[i], s2[i])

        for ele in baseStr:
            if ele in rep: ans.append(finder(ele))
            else: ans.append(ele)
            
        return "".join(ans)