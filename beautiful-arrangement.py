class Solution:
    def countArrangement(self, n: int) -> int:
        mask = count = 0

        def permutation(curr):
            nonlocal mask, count
            if len(curr) == n:
                count += 1
                return

            for i in range(1, n + 1):
                if mask & (1<<(i-1)) == 0:
                    if (len(curr) + 1) % i == 0 or i % (len(curr) + 1) == 0:
                        mask |= 1 << i - 1
                        permutation(curr + [i])
                        mask ^= 1 << i - 1
                    
        permutation([])
        return count