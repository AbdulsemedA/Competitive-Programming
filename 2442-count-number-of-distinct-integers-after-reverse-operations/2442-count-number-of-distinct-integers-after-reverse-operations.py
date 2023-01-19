class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique = set()
        
        for number in nums:
            unique.add(number)
            reverse = 0
            
            while number > 0:
                remainder = number % 10
                reverse = (reverse * 10) + remainder
                number = number // 10
                
            unique.add(reverse)
        
        return len(unique)
        