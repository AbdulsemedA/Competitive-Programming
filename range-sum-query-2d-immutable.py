class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])       
        self.pfx = [[0] * (m+1) for _ in range(n+1)]
        
        for row in range(n):
            for col in range(m):
                self.pfx[row+1][col+1] = self.pfx[row][col+1] + self.pfx[row+1][col]               
                self.pfx[row+1][col+1] += matrix[row][col] - self.pfx[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        ans += (self.pfx[row2+1][col2+1] + self.pfx[row1][col1])        
        ans -= (self.pfx[row2+1][col1] + self.pfx[row1][col2+1])
        
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)