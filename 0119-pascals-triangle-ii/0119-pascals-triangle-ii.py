class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return [1] * (rowIndex + 1)
        
        else:
            prev_list = self.getRow(rowIndex - 1)
            curr_list = [1]
            
            for i in range(1, rowIndex):
                curr_list.append(prev_list[i-1] + prev_list[i])
                
            curr_list.append(1)
            
            return curr_list
        