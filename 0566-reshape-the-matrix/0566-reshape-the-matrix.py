class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if r * c != row * col:
            return mat
        else:
            flat = []
            answer = []
            for rw in range(row):
                for cl in range(col):
                    flat.append(mat[rw][cl])
            
            for i in range(r * c):
                if i % c == 0:
                    answer.append([])
                answer[-1].append(flat[i])
                
            return answer
                
                 

        