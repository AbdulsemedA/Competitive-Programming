class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = 0
        arr = []
        for i in s:
            arr.append(i)
        for i in range(len(arr)):
            if arr[i] in 'aeiou':
                arr[i] = 1
            else:
                arr[i] = 0 
        window = sum(arr[:k])
        maxi = window 
        for i in range(len(arr) - k):
            window = window - arr[i] + arr[i + k]
            maxi = max(window, maxi)
        return maxi
