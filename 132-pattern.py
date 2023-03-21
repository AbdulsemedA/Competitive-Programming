class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        mini = float('-inf')
        for i in range(n-1, -1, -1):
            if nums[i] < mini:
                return True
            while stack and nums[i] > stack[-1]:
                mini = stack.pop()
            stack.append(nums[i])
        return False