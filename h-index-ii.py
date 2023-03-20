class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        size = right = len(citations)
        
        while left <= right:
            mid = left + (right - left) // 2
            print(left, mid, right)

            if mid != 0:
                if mid > citations[size - mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if sum(citations) != 0:
                    return 1
                return 0
        mid = right + (left - right) // 2
        
        return mid