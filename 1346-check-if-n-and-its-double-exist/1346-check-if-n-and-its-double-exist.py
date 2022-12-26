class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_hmap = dict()
        
        for index,num in enumerate(arr):
            if num not in num_hmap:
                num_hmap[num] = index
                
            if num / 2 in num_hmap and index != num_hmap[num / 2]:
                return True
            
            elif num * 2 in num_hmap and index != num_hmap[num * 2]:
                return True
            
        return False
        