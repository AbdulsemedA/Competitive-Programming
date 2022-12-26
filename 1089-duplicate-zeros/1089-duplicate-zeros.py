class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        new_arr = [0] * size
        new_index = 0
        index = 0
        
        while new_index < size:
            if arr[index] != 0:
                new_arr[new_index] = arr[index]
                new_index += 1
            else:
                new_index += 2
                
            index += 1
        
        arr.clear()
        arr.extend(new_arr)
                
        