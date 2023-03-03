class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        circ = nums + nums
        stack = []

        for index in range(len(circ)):
            while stack and circ[index] > circ[stack[-1]]:
                ind = stack.pop()

                if ind >= len(nums):
                    continue

                result[ind] = circ[index]

            stack.append(index)
            
        return result