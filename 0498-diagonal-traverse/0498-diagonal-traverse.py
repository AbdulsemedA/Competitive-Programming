class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        Hsize = len(mat)
        Lsize = len(mat[0])
        answer = []
        
        if Hsize < 2:
            return mat[0]
        
        for index in range(Hsize):
            current = []
            row = index
            col = 0
            while row > -1 and col < Lsize:
                current.append(mat[row][col])
                row -= 1
                col += 1
            answer.append(current)
        
        for index in range(1,Lsize,1):
            current = []
            row = Hsize - 1
            col = index
            while col < Lsize and row > -1:
                current.append(mat[row][col])
                row -= 1
                col += 1
            answer.append(current)
        
        for index in range(len(answer)):
            if index % 2 != 0:
                answer[index] = answer[index][::-1]
                
        return [item for sublist in answer for item in sublist]
        