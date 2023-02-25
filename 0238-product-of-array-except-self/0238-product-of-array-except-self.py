class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left = [1] + nums
        right = nums + [1]
        right.reverse()
        forward = backward = 1
        
        for i in range(2,n+1):
            backward = right[i-1]
            right[i] *= backward
            
            forward = left[i-1]
            left[i] *= forward
        
        for i in range(1,len(left)):
            answer[i-1] = left[i-1] * right[len(right) - 1 - i]
            
        return answer
        