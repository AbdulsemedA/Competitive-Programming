class Solution:
    def countOrders(self, n: int) -> int:
        base = 1
        curr = 2 * n - 1
        
        while curr > 1:
            base *= curr
            curr -= 2
        
        base *= factorial(n)
        return base % (10 ** 9 + 7)