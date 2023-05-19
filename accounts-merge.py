class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep, temp, ans = {}, [], []
        
        def finder(x):
            while x != rep[x][1]: 
                x = rep[x][1]
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)
            

            if fst != snd:
                if rep[fst][2] < rep[snd][2]:
                    rep[fst][1] = snd
                    rep[snd][2] += 1 + rep[fst][2]
                else:
                    rep[snd][1] = fst
                    rep[fst][2] += 1 + rep[snd][2]
            
        for ele in accounts:
            name = ele[0]
            
            for e1 in range(1, len(ele)):
                rep[ele[e1]] = [name, ele[e1], 0]
        
        
        
        for ele in accounts:
            for e1 in range(1, len(ele) - 1):
                for e2 in range(e1 + 1, len(ele)):
                    union(ele[e1], ele[e2])
                    
        for k, v in rep.items():
            temp.append([v[0], finder(v[1]) , k])
        
        temp.sort()
        curr, idx = "", -1


        for name, par, email in temp:
            if par != curr:
                ans.append([name])
                idx += 1
                curr = par
            ans[idx].append(email)
        
        return ans