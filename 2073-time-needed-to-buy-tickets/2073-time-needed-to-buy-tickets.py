class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total, left, n = 0, 0, len(tickets)
        
        while tickets[k] > 0:
            if tickets[left % n]:
                tickets[left % n] -= 1
                total += 1
                
            left += 1
        
        return total
        