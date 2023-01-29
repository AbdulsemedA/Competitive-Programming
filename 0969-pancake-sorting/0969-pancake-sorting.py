class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        flips = []
        
        for idx in range(size):
            max_val = max(arr[:size - idx])
            max_idx = arr.index(max_val) + 1
            
            arr[:max_idx] = reversed(arr[:max_idx])
            flips.append(max_idx)
            
            arr[:size - idx] = reversed(arr[:size - idx])
            flips.append(size - idx)
                
        return flips
        