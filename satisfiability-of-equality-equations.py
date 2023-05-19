class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {chr(i): chr(i) for i in range(97, 123)}
        
        def finder(x):
            while x != rep[x]:
                x = rep[x]
            
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            rep[fst] = rep[snd] = snd

        for ele in equations:
            fst, ch1, ch2, snd = ele
            if ch1 == ch2: union(fst, snd)
        
        for ele in equations:
            fst, ch1, ch2, snd = ele
            if ch1 != ch2: 
                if finder(fst) == finder(snd):
                    return False
        
        
        return True