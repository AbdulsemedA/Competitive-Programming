class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = len(nums1), len(nums2)
        diff = abs(a - b)
        
        if a < b:
            nums1.extend([0] * (b - a))
        else:
            nums2.extend([0] * (a - b))
        
        n = max(a, b)
        grid = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    grid[i][j] = grid[i+1][j+1] + 1
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]