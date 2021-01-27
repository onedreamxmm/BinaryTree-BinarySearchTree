'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
'''

class Solution:
    def isBST(self, root, low=-float(inf), high=float(inf)):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.isBST(root.left, low, root.val) and self.isBST(root.right, root.val, high)
