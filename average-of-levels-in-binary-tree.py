# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        def bfs(node):
            queue = deque([root])
            
            while queue:
                sums = size = 0

                for i in range(len(queue)):
                    curr = queue.popleft()
                    sums += curr.val
                    size += 1
                    
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    
                ans.append(sums/size)

        bfs(root)
        return ans