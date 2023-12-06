# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        Hmap = defaultdict(int)
        answer = set()

        def dfs(curr_node):
            if not curr_node: return '#'
            path = ''

            if not curr_node.left and not curr_node.right:
                path += str(curr_node.val)
                Hmap[path] += 1
                
                if Hmap[path] == 2:
                    answer.add(curr_node)

                return str(curr_node.val)
            
            path += str(curr_node.val)
            path += '.' + dfs(curr_node.left)
            path += '.' + dfs(curr_node.right)
            Hmap[path] += 1

            if Hmap[path] == 2:
                answer.add(curr_node)
            
            return path
        
        dfs(root)
        return answer