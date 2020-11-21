# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    passed = False

    def searchTree(self, root: TreeNode) -> bool:
        if root == None:
            return True

        if root.left == root.right == None:
            if not Solution.passed:
                return True
            else:
                return root.val
        elif not Solution.passed:
            Solution.passed = True
        left = right = None

        if root.left:
            left = Solution.searchTree(self, root.left)

        if root.right:
            right = Solution.searchTree(self, root.right)

        if type(left) is list:
            return [*left, root.val, *right]#, left < root.val < right
        else:
            return [left, root.val, right]

    def isValidBST(self, root: TreeNode) -> bool:
        l = Solution.searchTree(self, root)
        l = [i for i in l if i is not None]
        return sorted(l) == l

r = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
t = TreeNode(val=5, left=TreeNode(val=1, left=TreeNode(val=-1), right=TreeNode(val=3)), right=TreeNode(val=7, left=TreeNode(6), right=TreeNode(8)))
s = Solution()
print(s.isValidBST(t))