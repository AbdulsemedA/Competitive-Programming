class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        answer, L = self.builder(n)
        return answer[k - 1]
    
    def builder(self, n: int):
        if n == 1: return ["0"], 1
        s_bits, L = self.builder(n - 1)
        new_bits = s_bits + ["1"]

        for i in range(L-1,-1,-1):
            add = "0" if int(s_bits[i]) else "1"
            new_bits.append(add)
        
        return new_bits, 2 * L + 1