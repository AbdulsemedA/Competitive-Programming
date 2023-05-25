class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 1
        for idx in range(len(arr)):
            if arr[idx] >= curr:
                arr[idx] = curr
                curr += 1

        return arr[-1]