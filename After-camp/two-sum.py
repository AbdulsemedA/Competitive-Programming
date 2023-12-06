class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        answer = []

        for idx, num in enumerate(nums):
            if target - num in Hmap:
                answer += [idx, Hmap[target - num]]
                return answer

            Hmap[num] = idx