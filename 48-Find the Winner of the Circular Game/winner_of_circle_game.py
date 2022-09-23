class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        game = []
        for i in range(1,n+1):
            game.append(i)
        current = 0
        for i in range(n-1):
            current = (current + k-1) % len(game)
            game.pop(current)
        return game[0]
