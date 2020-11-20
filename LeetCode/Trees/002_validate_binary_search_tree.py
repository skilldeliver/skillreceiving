# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        if root.left == root.right == None:
            return True

        left = right = None
        if root.left:
            left = Solution.isValidBST(self, root.left)

        if left is False:
            return False

        if left is not None and root.left.val >= root.val:
            return False

        if root.right:
            right = Solution.isValidBST(self, root.right)

        if right is False:
            return False

        if right is not None and root.right.val <= root.val:
            return False
        return True

t = TreeNode(val=5, left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(3), right=TreeNode(6)))
s = Solution()
print(s.isValidBST(t))