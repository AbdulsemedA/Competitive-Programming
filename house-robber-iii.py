# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)

        def dp(node):
            if not node: return 0
            if not node.left and not node.right: return node.val
            if node in memo: return memo[node]
            c1 = node.val
            c2 = 0

            if node.left:
                c1 += dp(node.left.left) + dp(node.left.right)
                c2 = dp(node.left)
            if node.right:
                c1 += dp(node.right.left) + dp(node.right.right)
                c2 += dp(node.right)
            
            memo[node] = max(c1, c2)

            return memo[node]
        
        return dp(root)