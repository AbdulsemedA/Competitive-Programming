class Solution:
    def convert(self, s: str, numRows: int) -> str:
        gap = 2 * numRows - 2
        right = 0
        size = len(s)
        answer = []
        if numRows == 1 or size < numRows:
            return s
        
        for index in range(numRows):
            answer.append([s[index]])
            l_gap = index + gap - right
            r_gap = index + gap
            
            while l_gap < size or r_gap < size:
                if index != numRows - 1:
                    if l_gap < size:
                        answer[index].append(s[l_gap])
                if index != 0:
                    if r_gap < size:
                        answer[index].append(s[r_gap])
                        
                l_gap += gap
                r_gap += gap
                
            right += 2
            
        return ''.join([''.join(item) for item in answer])
                    
                
                
                
        
        
        