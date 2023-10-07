class Solution:
    def knightDialer(self, n: int) -> int:
        direction = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        matrix = [[1] * 3 for _ in range(4)]
        matrix[3][0] = matrix[3][2] = 0
        hMap= {}

        def inbound(x, y):
            return 0 <= x < 4 and 0 <= y < 3

        def dialer(curr, x, y):
            if curr == n:
                return 1
            
            if (curr, x, y) in hMap:
                return hMap[(curr, x, y)]
            
            ans = 0
            for uc, vc in direction:
                ux, uy = x + uc, y + vc

                if inbound(ux,uy) and matrix[ux][uy]:
                    ans += dialer(curr + 1, ux, uy)
            
            hMap[(curr, x, y)] = ans
            return ans
        
        total = 0
        for i in range(4):
            for j in range(3):
                if matrix[i][j]:
                    total += dialer(1, i, j)
        
        return total % (10 ** 9 + 7)