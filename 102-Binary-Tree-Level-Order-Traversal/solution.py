# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = []
        ret = []
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size+1):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                elif node.right:
                    queue.append(node.right)
            ret.append(level)
        return ret
                    
                    