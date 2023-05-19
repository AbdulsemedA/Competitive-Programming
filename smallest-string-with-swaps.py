class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        answer = ["" for _ in s]
        rep = {i: [i, 0] for i in range(len(s))}
        temp, ans = [], []
        
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

        for src, des in pairs:
            union(src, des)
        
        for k, v in rep.items():
            temp.append([finder(v[0]), k])
        
        temp.sort()
        curr = idx = -1

        for par, ele in temp:
            if par != curr:
                ans.append([[],[]])
                idx += 1
                curr = par

            ans[idx][0].append(ele)
            ans[idx][1].append(s[ele])
        
        for ele in range(len(ans)):
            ans[ele][0].sort()
            ans[ele][1].sort()

            for ch in range(len(ans[ele][0])):
                answer[ans[ele][0][ch]] = ans[ele][1][ch]

        return "".join(answer)