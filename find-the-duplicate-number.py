class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictn = dict()
        for i in nums:
            if i not in dictn:
                dictn[i] = 1
            else:
                dictn[i] += 1
        freq = {v: k for k,v in dictn.items()}
        return freq[max(freq)]