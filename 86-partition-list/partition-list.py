# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy_first_half = ListNode(0)
        dummy_last_half = ListNode(0)
        first_half = dummy_first_half
        last_half = dummy_last_half
        
        while head:
            if head.val < x:
                first_half.next = head
                first_half = first_half.next
            else:
                last_half.next = head
                last_half = last_half.next
            head = head.next
        first_half.next = dummy_last_half.next
        last_half.next = None
        return dummy_first_half.next
