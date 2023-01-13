class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        
        for local in range(len(grid) - 2):
            answer.append([])
            for loc in range(len(grid) - 2):
                maxi = float("-inf")
                for row in range(local, local + 3):
                    for col in range(loc, loc + 3):
                        maxi = max(maxi,grid[row][col])
                answer[-1].append(maxi)
        
        return answer
                    
        
        