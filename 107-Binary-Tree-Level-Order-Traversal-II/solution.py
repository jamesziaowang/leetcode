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
        queue.append(root)
        level = []
        ret = []
        while queue:
            n = len(queue)
            for i in range(0,n):
                temp = queue.pop(0)
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                elif temp.right:
                    queue.append(temp.right)
            ret.insert(0,level)
        return ret
                
            
            