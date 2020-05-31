""" Construct Binary Search Tree from Preorder Traversal """
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root_head=TreeNode(preorder[0])
        root=root_head
        len_preorder=len(preorder)
        index=1
        while index<len_preorder:
            element=preorder[index]
            root=root_head
            prev=root
            while root:
                if element>=root.val:
                    prev=root
                    root=root.right
                elif element<root.val:
                    prev=root
                    root=root.left
                    
            if element>=prev.val:
                prev.right=TreeNode(element)
            else:
                prev.left=TreeNode(element)
            index+=1
        return root_head