# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        holder = None
        if root == None:
            return root
            
        elif root.left or root.right:
            holder = root.left
            root.left = root.right
            root.right = holder
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root