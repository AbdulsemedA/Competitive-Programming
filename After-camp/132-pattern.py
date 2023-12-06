class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = nums[0]
        stack = [(mini, nums[0])]
        n = len(nums)

        for idx in range(1, n):
            while stack and stack[-1][1] <= nums[idx]:
                stack.pop()
            
            if stack and nums[idx] > stack[-1][0]:
                return True
            
            stack.append((mini, nums[idx]))
            mini = min(mini, nums[idx])

        return False