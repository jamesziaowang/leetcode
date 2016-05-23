# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetric(root.left,root.right)
        
    def isSymmetric(l,r):
        if l and r:
            return l.val==r.val and isSymmetric(l.left,r.right) and isSymmetric(l.right, r.left)
        else:
            return not l and not r
            
                                    