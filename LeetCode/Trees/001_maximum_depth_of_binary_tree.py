# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node: TreeNode, depth: int) -> int:
        if node == None:
            return 0

        if node.left == node.right == None:
            return depth

        depth_left = depth_right = 0
        if node.left:
            depth_left = Solution.traverseTree(self, node.left, depth + 1)
        if node.right:
            depth_right = Solution.traverseTree(self, node.right, depth + 1)

        if depth_left >= depth_right:
            return depth_left
        else:
            return depth_right

    def maxDepth(self, root: TreeNode) -> int:
        return Solution.traverseTree(self, root, 1)y

s = Solution()
t = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(s.traverseTree(t, 1))