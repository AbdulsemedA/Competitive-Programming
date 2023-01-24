class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i, val in enumerate(numbers):
            if target - val in hmap:
                return [hmap[target - val] + 1, i + 1]
            else:
                hmap[val] = i
                
        