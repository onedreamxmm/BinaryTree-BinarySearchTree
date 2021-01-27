'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

time complexity: O(n)
space complexity: O(n) in the worst case of completely unbalanced tree; if the trees are balanced binary tree, the space complexity would be O(log(n))

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, one: TreeNode, two: TreeNode) -> bool:
        if not one and not two:
            return True
        if not one or not two:
            return False
        if one.val != two.val:
            return False
        return self.isSameTree(one.left, two.left) and self.isSameTree(one.right, two.right)