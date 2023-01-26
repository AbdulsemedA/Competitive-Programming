class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        count = 0
        
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            count += 1
            right -= 1
        
        return count
        
        