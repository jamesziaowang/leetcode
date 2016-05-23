# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def help(self,l,r):
        if l and r:
            return l.val==r.val and help(l.left, r.right) and help(l.right, r.left)
        elif not l and not r:
            return True
            
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.help(self,root.left, root.right)
        
        
            
                                    