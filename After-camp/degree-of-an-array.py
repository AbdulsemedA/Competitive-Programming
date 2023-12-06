class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        freq = Counter(nums)
        maxi = max(freq.values())
        Hmap = {}
        min_len = n

        while right < n:
            Hmap[nums[right]] = 1 + Hmap.get(nums[right], 0)
            right += 1
            
            while left < right and max(Hmap.values()) >= maxi:
                Hmap[nums[left]] -= 1
                if not Hmap[nums[left]]:
                    del Hmap[nums[left]]
                left += 1
                min_len = min(min_len, right - left + 1)

        return min_len
            