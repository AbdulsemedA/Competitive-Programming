class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        values = {0: 1}
        result = 0
        current = 0
        for i in nums: 
            current += i
            if current % k in values: 
                result += values[current % k]
                values[current % k] += 1        
            else:
                values[current % k] = 1
        return result