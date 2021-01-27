'''
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].


'''

class Solutiuon:
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.sum += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        self.sum = 0
        dfs(root)
        return self.sum

