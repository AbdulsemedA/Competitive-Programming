# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []

        def dfs(curr_node):
            if not curr_node: return

            curr_node.left = dfs(curr_node.left)
            curr_node.right = dfs(curr_node.right)

            if curr_node.val in to_delete:
                if curr_node.left: ans.append(curr_node.left)
                if curr_node.right: ans.append(curr_node.right)
                return
            
            return curr_node
        
        if dfs(root): ans.append(root)
        return ans