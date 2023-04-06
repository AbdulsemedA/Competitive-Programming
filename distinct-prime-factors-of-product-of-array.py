class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        unique = set()
        length = 0
        
        for num in nums:
            factor = 2
            
            while factor * factor <= num:
                if num % factor == 0:
                    if factor not in unique:
                        length += 1
                        unique.add(factor)
                    num //= factor
                else:
                    factor += 1

            if num != 1:
                if num not in unique:
                    length += 1
                    unique.add(num)

        return length