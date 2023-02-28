class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0 for i in range(1002)]
        
        for people, start, end in trips:
            prefix[start] += people
            prefix[end] -= people
        
        curr = 0
        
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        
        return max(prefix) <= capacity
        