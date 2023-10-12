# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, curr):
            if not node: return
            if not node.left and not node.right:
                if curr + node.val == targetSum:
                    result.append(path + [node.val])
                    return
            else:
                dfs(node.left, path + [node.val], curr + node.val)
                dfs(node.right, path + [node.val], curr + node.val)
        
        dfs(root, [], 0)
        return result