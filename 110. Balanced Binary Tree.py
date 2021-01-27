'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

'''

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)

    def isBalanced(self, root):
        if not root:
            return True
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
