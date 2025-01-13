# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        counter = 0
        pointer = head
        while pointer:
            counter += 1
            pointer = pointer.next
        position = counter - n
        if position == 0:
            return head.next
        counter = 1
        pointer = head
        while counter < position:
            pointer = pointer.next
            counter += 1
        if pointer.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = None
        return head
