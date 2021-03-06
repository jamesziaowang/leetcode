# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    
    
    def help(self, retStr, node):
        if node.left is None and node.right is None:
            self.ret += retStr,
        if node.left:
            self.help(retStr+"->"+ str(node.left.val),node.left)
        if node.right:
            self.help(retStr+"->"+ str(node.right.val),node.right)
    
    def binaryTreePaths(self, root):
        if not root: return []
        self.ret = []
        self.help(str(root.val),root)
        return self.ret
        