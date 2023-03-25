# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = 0
        
        def pathSum(root, curr, val):
            nonlocal counts
            if not root: return
            curr += root.val
            value = val.copy()
            value[curr] = 1 + value.get(curr, 0)

            if len(value) > 0 and curr == targetSum: counts += 1
            if curr - targetSum in val:
                counts += val[curr - targetSum]
            
            pathSum(root.left, curr, value)
            pathSum(root.right, curr, value)
            
        pathSum(root, 0, {})
        return counts