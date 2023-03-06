class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        size = 2**(n-1)
        if k > math.ceil(size/2):
            return self.invert(self.kthGrammar(n - 1, k - size//2))
        else:
            return self.kthGrammar(n-1, k)

    def invert(self, num):
        if num == 1:
            return 0
        return 1