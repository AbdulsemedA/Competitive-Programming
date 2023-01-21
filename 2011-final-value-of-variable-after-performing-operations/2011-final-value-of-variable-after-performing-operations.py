class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for item in operations:
            if item[1] == '+':
                x += 1
            else:
                x -= 1
        return x
        