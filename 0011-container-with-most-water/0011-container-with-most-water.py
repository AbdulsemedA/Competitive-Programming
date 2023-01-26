class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        left, right = 0 , n - 1
        
        while left < right:
            current = (right - left) * min(height[right],height[left])
            max_area = max(max_area, current)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area
                
            
        