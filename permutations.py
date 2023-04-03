class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        mask = 0 

        def backtrack(curr):
            nonlocal mask
            if len(curr) == n:
                answer.append(curr[:])
                return

            for i in range(n):
                if (mask >> i) & 1 == 0:
                    mask |= 1 << i
                    # curr.append(nums[i])
                    backtrack(curr + [nums[i]])
                    mask ^= 1 << i
                    # curr.pop()

        backtrack([])
        return answer