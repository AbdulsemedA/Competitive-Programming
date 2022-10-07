class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        left = [(prod:=prod*nums[v]) for v in range(len(nums))]
        prod = 1
        left.insert(0,1)
        right = [(prod:=prod*nums[v]) for v in range(len(nums)-1,-1,-1)]
        right.insert(0,1)
        answer = [1] * len(nums)
        for i in range(1,len(left)):
            answer[i-1] = left[i-1] * right[len(right) - 1 - i]
        return answer
