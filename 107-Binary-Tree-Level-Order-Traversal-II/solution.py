# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = []
        ret = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                temp = queue.pop(0)
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ret.insert(0,level)
        return ret
                
            
            