'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

But the following [1,2,2,null,3,null,3] is not:

time complexity: O(n) 最多对比你2/n次（n为node总数）
space Complexity: O(n) in the worst case, root左右分别是一个linked list, call stack的总数是2/n;若是balanced Binary Tree， 时间复杂度是O(log(n))
'''

class Solution:
    def isMirror(self, one, two):
        if (not one) and (not two):
            return True
        if (not one) or (not two):
            return False
        if one.val != two.val:
            return False
        return self.isMirror(one.left, two.right) and self.isMirror(one.right, two.left)

    def isSymmetric(self, root):
        return self.isMirror(root, root)

