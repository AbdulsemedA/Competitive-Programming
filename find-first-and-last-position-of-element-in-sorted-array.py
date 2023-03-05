class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]
        found = False

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                found = True
                break
        
        if found:
            left = right = mid
            while left >= 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1

            ans[0] = left + 1
            ans[1] = right - 1
                
        return ans