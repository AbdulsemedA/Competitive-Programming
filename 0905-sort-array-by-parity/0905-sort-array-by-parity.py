class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0] * size
        first = 0
        last = size - 1
        
        for num in nums:
            if num % 2 == 0:
                result[first] = num
                first += 1
            else:
                result[last] = num
                last -= 1
                
        return result

        