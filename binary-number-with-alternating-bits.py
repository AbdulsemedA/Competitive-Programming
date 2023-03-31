class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 2
        while n > 0:
            temp = n & 1
            if temp == prev: return False
            n >>= 1
            prev = temp
        return True