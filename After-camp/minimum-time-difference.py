class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float('inf')
        n = len(timePoints)

        for i in range(n):
            H, M = map(int, timePoints[i].split(":"))
            timePoints[i] = H * 60 + M
        
        timePoints.sort()
        
        for idx in range(1, n):
            ans = min(ans, timePoints[idx] - timePoints[idx - 1])
        
        ans = min(ans, 1440 + timePoints[0] - timePoints[-1])        
        return ans