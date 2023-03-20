class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        string_len = 2**n - 1
        if n == 1:
            return "0"
        elif k < math.ceil(string_len / 2):
            return self.findKthBit(n-1,k)
        elif k > math.ceil(string_len / 2):
            return self.invert(self.findKthBit(n-1, string_len - k+1))
        else:
            return "1"
    
    def invert(self, ch):
        if ch == "0":
            return "1"
        return "0"