class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, m - 1
        first, last = 0, n - 1
        index = -1
        
        while low <= high:
            middle = (low + high) // 2
            if matrix[middle][0] <= target and matrix[middle][n - 1] >= target:
                index = middle
                break
            elif matrix[middle][n - 1] > target:
                high = middle - 1
            else:
                low = middle + 1
                
        
        while first <= last:
            middle = (first + last) // 2
            if matrix[index][middle] == target:
                return True
            elif matrix[index][middle] < target:
                first = middle + 1
            else:
                last = middle - 1
        
        
                
                