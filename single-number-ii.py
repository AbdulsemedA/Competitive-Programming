class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(32):
            count = 0
            for ele in nums:
                if ele & (1<<i):
                    count += 1
            if count % 3:
                num += 2 ** i
        negatives = 0
        for i in nums: 
            if i < 0: negatives += 1
        if negatives % 3:
            num -= 1<<32
        return num