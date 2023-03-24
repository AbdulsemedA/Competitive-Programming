class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()

        def nonDecre(idx, curr):
            if len(curr) > 1: answer.add(tuple(curr[:]))
            if idx == len(nums): return

            if not curr or curr[-1] <= nums[idx]:
                nonDecre(idx + 1, curr + [nums[idx]])
            nonDecre(idx + 1, curr)

        nonDecre(0, [])
        return answer