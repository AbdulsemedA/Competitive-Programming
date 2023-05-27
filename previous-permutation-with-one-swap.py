class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        idx = -1

        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                idx = i - 1
                break

        if idx == -1: return arr

        for j in range(n - 1, idx, -1):
            if arr[j] < arr[idx] and arr[j] != arr[j - 1]:
                arr[j], arr[idx] = arr[idx], arr[j]
                break
        
        return arr