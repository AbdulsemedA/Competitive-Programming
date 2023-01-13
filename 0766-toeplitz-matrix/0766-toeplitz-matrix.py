class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        Hmap = {}
        
        for rw in range(row):
            for cl in range(col):
                if rw - cl in Hmap:
                    if matrix[rw][cl] != Hmap[rw - cl]:
                        return False
                else:
                    Hmap[rw - cl] = matrix[rw][cl]
        
        return True
        
        
        