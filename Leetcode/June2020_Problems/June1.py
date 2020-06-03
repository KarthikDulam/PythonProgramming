'''Invert Binary Tree'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        stack = []
        stack.append(root)
        while len(stack) != 0:
            t = stack[-1]
            stack = stack[:-1]
            temp = t.left
            t.left = t.right
            t.right = temp
            if t.right != None:
                stack.append(t.right)
            if t.left != None:
                stack.append(t.left)
        return root