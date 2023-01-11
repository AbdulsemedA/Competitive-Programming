class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        grid = [[] for _ in range(len(strs[0]))]
        for j in range(len(grid)):
            for item in strs:
                grid[j].append(item[j])
        counter = 0
        for item in grid:
            if item == sorted(item):
                continue
            counter += 1
        return counter
            
        