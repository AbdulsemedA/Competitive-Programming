class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi = count = 0
        unique = set()
        for i in nums: maxi |= i
        
        def subsets(idx, curr, num):
            nonlocal count, maxi, unique
            if tuple(num) not in unique and curr == maxi:
                count += 1
            unique.add(tuple(num))
            if idx == len(nums) - 1:
                return

            subsets(idx + 1, curr | nums[idx + 1], num + [idx + 1])
            subsets(idx + 1, curr, num)
        
        subsets(-1, 0, [])
        return count