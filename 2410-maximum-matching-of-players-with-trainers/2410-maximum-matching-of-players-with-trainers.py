class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p1 = p2 = total = 0
        
        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                total += 1
                p1 += 1
                p2 += 1
            else:            
                p2 += 1
        
        return total
        
            
        
        