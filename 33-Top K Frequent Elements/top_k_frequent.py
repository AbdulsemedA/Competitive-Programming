class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dect = Counter(nums)
        ans = list(dect.values())
        nums = list(dict.fromkeys(nums))
        result = []
        for i in range(k):
            result.append(nums[ans.index(max(ans))])
            nums.pop(ans.index(max(ans)))
            ans.pop(ans.index(max(ans)))
        return result
