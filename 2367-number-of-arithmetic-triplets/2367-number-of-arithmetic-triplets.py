class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        diff_dict = {}
        triples = 0
        n = len(nums)
        
        for i in nums:
            diff_dict[i] = 0
        
        for i in diff_dict:
            if i + diff in diff_dict and i + 2 * diff in diff_dict:
                triples += 1
            
        
        # print(diff_dict)
        return triples