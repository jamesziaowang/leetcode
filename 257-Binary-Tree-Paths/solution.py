# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    
    def help(self, nodeList, node):
        if node: nodeList.append(str(node.val))
        if node.left:
            nodeList.append("->")
            self.help(nodeList,node.left)
        elif node.right:
            nodeList.append("->")
            self.help(nodeList,node.right)
        else:
            return nodeList
    
    def binaryTreePaths(self, root):
        if not root:
            return []
        ret = []
        l = []
        r = []
        l.append(root.val)
        r.append(root.val)
        if root.left: 
            nodeList.append("->")
            ret.append(self.help(l,root.left))
        elif root.right:
            nodeList.append("->")
            ret.append(self.help(r,root.right))
        else: ret.append(str(root.val))
        return ret
        