class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peaks = []
        n = len(arr)
        for item in range(1, n - 1,1):
            if arr[item] > arr[item - 1] and arr[item] > arr[item + 1]:
                i = 0
                flag = True
                while i < item:
                    if arr[i] < arr[i+1]:
                        i += 1
                    else:
                        flag = False
                        break
                    
                i = item
                while i < n - 1:
                    if arr[i] > arr[i+1]:
                        i += 1
                    else:
                        flag = False
                        break
                if flag:
                    peaks.append(item)
                    
        if not(peaks):
            return False
        return True
        