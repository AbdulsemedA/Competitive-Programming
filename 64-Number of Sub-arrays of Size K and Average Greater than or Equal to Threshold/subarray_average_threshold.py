class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total_sub = 0
        window = sum(arr[:k])
        if(window / k >= threshold):
                total_sub += 1
        for i in range(len(arr) - k):
            window = window - arr[i] + arr[i + k]
            if(window / k >= threshold):
                total_sub += 1
        return total_sub
