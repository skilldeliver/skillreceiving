# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, root: TreeNode) -> bool:
        if root.right == root.left == None:
            return root.val

        left = right = None
        if root.left:
            left = Solution.traverseTree(self, root.left)
        if root.right:
            right = Solution.traverseTree(self, root.right)

        print(left, root.val, right)
        return left, root.val, right

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        tree = Solution.traverseTree(self, root)
        return tree == tree[::-1]

r = TreeNode(1, left=TreeNode(2), right=TreeNode(2))
l = TreeNode(5, left=TreeNode(4, right=TreeNode(1, left=TreeNode(2))), right=TreeNode(1, right=TreeNode(4, left=TreeNode(2))))

# t = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(2, right=TreeNode(3, left=TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(2, right=TreeNode(3))))))
s = Solution()
print(s.isSymmetric(l))