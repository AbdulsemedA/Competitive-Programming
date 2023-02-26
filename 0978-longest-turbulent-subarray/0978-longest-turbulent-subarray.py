class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxi, n = 1, len(arr)
        left, right = 0, 1
        down = up = 0
        
        while right < n:
            if arr[right] > arr[right - 1]:
                if not up:
                    up, down = 1, 0
                else:
                    maxi = max(maxi, right - left)
                    left = right - 1
                right += 1
                
            elif arr[right] < arr[right - 1]:
                if not down:
                    down, up = 1, 0
                else:
                    maxi = max(maxi, right - left)
                    left = right - 1
                right += 1
                
            else:
                maxi = max(maxi, right - left)
                left = right
                right += 1
            if right == n and down or up:
                maxi = max(maxi, right - left)
        
        return maxi
        