'''Cousins in Binary Tree'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # values of nodes are unique - there is no overwritting issue, so we can use maps
    def __init__(self):
        self.depths = {}
        self.parents = {}
    
    def DFS(self, root, parent = None, counter = 0):
        if root is None:
            return
        # add depth value of this node
        self.depths[root.val] = counter
        # add record about parent of this node
        self.parents[root.val] = parent
        # check left and right subtree
        self.DFS(root.left, root, counter+1)
        self.DFS(root.right, root, counter+1)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.depths = {}
        self.parents = {}
        self.DFS(root)
        # check if depths are the same and if they don't have the same parent
        return self.depths[x] == self.depths[y] and \
            self.parents[x] != self.parents[y]
        