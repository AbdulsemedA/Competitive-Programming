# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1