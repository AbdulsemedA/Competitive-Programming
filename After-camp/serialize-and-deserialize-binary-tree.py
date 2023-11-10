# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        serial = ''

        if root:
            queue = deque([root])

            while queue:
                node = queue.popleft()
                if node == ' ':
                    serial += node
                else:
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(' ')
                    
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(' ')
                    
                    serial += str(node.val)

                serial += ','
        
        return serial

    def deserialize(self, data):
        if not data: return None
        arr = list(map(str, data.split(',')))
        while arr[-1] == "" or arr[-1] == " ": arr.pop()
        n = len(arr)
        
        root = TreeNode(arr[0])
        queue = deque([(root, 0)])
        nextn = 1
        while queue:
            node, idx = queue.popleft()
            left = nextn
            right = left + 1
            
            if left < n:
                if arr[left] != ' ':
                    node.left = TreeNode(arr[left])
                    queue.append((node.left, left))
                nextn += 1

            if right < n:
                if arr[right] != ' ':
                    node.right = TreeNode(arr[right])
                    queue.append((node.right, right))
                nextn += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))