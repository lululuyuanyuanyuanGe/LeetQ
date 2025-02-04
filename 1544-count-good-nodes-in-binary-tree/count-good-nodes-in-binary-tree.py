# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderGoodNodes(self, root, max_val = float('-inf')):
        if not root:
            return 0

        good = 1 if root.val >= max_val else 0
        max_val = max(root.val, max_val)

        return good + self.preorderGoodNodes(root.left, max_val) + self.preorderGoodNodes(root.right, max_val)
    def goodNodes(self, root: TreeNode) -> int:
        return self.preorderGoodNodes(root)