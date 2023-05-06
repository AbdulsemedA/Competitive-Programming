# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        
        def bfs(queue, res, visited):
            dis = -1
            while queue:
                size = len(queue)
                dis += 1
                for _ in range(size):
                    cur = queue.popleft()
                    if dis == k:
                        res.append(cur)
                    for node in graph[cur]:
                        if node not in visited:
                            visited.add(node)
                            queue.append(node)
            return res

        return bfs(deque([target.val]), [], set([target.val]))