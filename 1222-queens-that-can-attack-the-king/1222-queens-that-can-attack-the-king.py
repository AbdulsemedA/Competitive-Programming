class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        KingMoves = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        answer = []
        queen = set()
        
        for item in queens:
            queen.add(tuple(item))
        
        for index in KingMoves:
            x = king[0]
            y = king[1]
            while x > -1 and y > -1 and x < 8 and y < 8:
                x += index[0]
                y += index[1]

                if (x, y) in queen:
                    answer.append([x,y])
                    break
        
        return answer
            
            
        