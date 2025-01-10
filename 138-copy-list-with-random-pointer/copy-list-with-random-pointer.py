"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            copy_node = Node(current.val)
            copy_node.next = current.next
            current.next = copy_node
            current = current.next.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        original = head
        copy = head.next
        copy_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        
        return copy_head