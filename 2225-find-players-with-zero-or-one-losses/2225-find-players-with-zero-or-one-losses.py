class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        losser = {}
        answer = [[],[]]
        
        for index in range(len(matches)):
            winner[matches[index][0]] = 1 + winner.get(matches[index][0],0)
            losser[matches[index][1]] = 1 + losser.get(matches[index][1],0)
        
        for item in winner:
            if item not in losser:
                answer[0].append(item)
                
        for item in losser:
            if(losser[item] == 1):
                answer[1].append(item)
                
        for item in answer:
            item.sort()
            
        return answer
        