# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        # Implement the algorithm here
        result = []
        queue = [root]  # Use a list to simulate a queue

        while queue:
            level_sum = 0
            level_count = len(queue)
            next_queue = []

            for node in queue:
                level_sum += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            result.append(level_sum / level_count)
            queue = next_queue

        return result