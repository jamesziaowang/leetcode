# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        minLeft = self.minDepth(root.left)
        minRight = self.minDepth(root.right)
        if minLeft == 0 or minRight == 0:
            return minLeft+1  if minLeft>=minRight else minRight +1
        return min(minLeft,minRight)+1