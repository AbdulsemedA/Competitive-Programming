class Solution:
    def simulator(self, nums, left, right, trn) -> List[int]:
        if left == right:
            if trn:
                return [nums[left],0]
            else:
                return [0,nums[left]]
        
        if trn:
            LHS = self.simulator(nums, left+1, right, False)
            LHS[0] += nums[left]
            RHS = self.simulator(nums, left, right-1, False)
            RHS[0] += nums[right]
            
            if RHS[0] > LHS[0]:
                return RHS
            else:
                return LHS
        else:
            LHS = self.simulator(nums, left+1, right, True)
            LHS[1] += nums[left]
            RHS = self.simulator(nums, left, right-1, True)
            RHS[1] += nums[right]

            if RHS[1] > LHS[1]:
                return RHS
            else:
                return LHS
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1
        score = self.simulator(nums, left, right, True)

        return score[0] >= score[1]