class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_freq = Counter(arr)
        size = int(len(arr)/2)
        frequency = sorted(arr_freq.values(),reverse=True)
        res = 0
        for i in frequency:
            if size > 0:
                size-=i
                res+=1
        return res
