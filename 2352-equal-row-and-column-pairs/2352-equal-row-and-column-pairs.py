class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dictionaryRow = {}
        dictionaryCol = {}
        counter = 0
        
        row_size = len(grid)
        col_size = len(grid[0])
        
        for item in range(row_size):
            temp = str(grid[item])
            dictionaryRow[temp] = 1 + dictionaryRow.get(temp,0)
            
        
        for col in range(col_size):
            temp = []
            for row in range(row_size):
                temp.append(grid[row][col])
            dictionaryCol[str(temp)] = 1 + dictionaryCol.get(str(temp),0)
        
        for item in dictionaryRow:
            if item in dictionaryCol:
                counter += dictionaryRow[item] * dictionaryCol[item]
        
        return counter
                
                
                
        