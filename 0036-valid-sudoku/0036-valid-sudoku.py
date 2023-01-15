class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    row_map[row].append(int(board[row][col]))
                    col_map[col].append(int(board[row][col]))
                
        for item in row_map:
            if len(set(row_map[item])) != len(row_map[item]):
                return False
            
        for item in col_map:
            if len(set(col_map[item])) != len(col_map[item]):
                return False
                
        for rows in range(0,9,3):
            for columns in range(0,9,3):
                unique = set()
                counter = 0
                for row in range(rows, rows + 3):
                    for col in range(columns, columns + 3):
                        if board[row][col] != ".":
                            unique.add(int(board[row][col]))
                            counter += 1    
                if len(unique) != counter:
                    return False
        
        return True