# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nums = []
        def columnTrav(root, col, depth, nums):
            if not root: return 0
            nums.append((col, depth, root.val))

            columnTrav(root.left, col - 1, depth + 1, nums)
            columnTrav(root.right, col + 1, depth + 1, nums)
        
        columnTrav(root, 0, 0, nums)
        order = sorted(nums, key = lambda x: (x[0], x[1], x[2]))
        curr = 1001
        answer = []

        for x in order:
            if x[0] != curr:
                answer.append([])
            answer[-1].append(x[2])
            curr = x[0]
        
        return answer