class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.add((row,col))
                    
        for item in zeros:
            if sum(matrix[item[0]]) != 0:
                for index in range(len(matrix[0])):
                    matrix[item[0]][index] = 0
            if sum([matrix[x][item[1]] for x in range(len(matrix))]):
                for index in range(len(matrix)):
                    matrix[index][item[1]] = 0
        
        