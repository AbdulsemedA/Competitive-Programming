class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        def subset(idx, num):
            if idx == n:
                subsets.append(num)
                return
            subset(idx + 1, num + [nums[idx]])
            subset(idx + 1, num)
        subset(0, [])
        return subsets