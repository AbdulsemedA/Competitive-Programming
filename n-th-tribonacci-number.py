class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0] * 38
        seq[0] = 0
        seq[1] = seq[2] = 1

        for i in range(3, 38):
            seq[i] = seq[i-1] + seq[i-2] + seq[i-3]
        
        return seq[n]