class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: x[2])
        rep = {i: i for i in range(n)}
        rep[0] = firstPerson

        def finder(x):
            while x != rep[x]:
                x = rep[x]
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst] == firstPerson or rep[snd] == firstPerson:
                    rep[fst] = rep[snd] = firstPerson
                else:
                    rep[fst] = snd
        
        n = len(meetings)
        idx = 0

        while idx < n:
            same_time = [meetings[idx]]
            while idx < n - 1 and meetings[idx][2] == meetings[idx + 1][2]:
                idx += 1
                same_time.append(meetings[idx])
            
            for frm, to, time in same_time:
                union(frm, to)
            
            for frm, to, time in same_time:
                if finder(frm) != firstPerson:
                    rep[frm] = frm
                    rep[to] = to
            
            idx += 1
        
        ans = []
        for ele in rep:
            if finder(ele) == firstPerson:
                ans.append(ele)
        
        return ans