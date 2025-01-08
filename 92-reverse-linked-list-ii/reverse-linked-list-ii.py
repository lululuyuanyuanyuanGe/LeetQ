# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
    
        list_vals = []
        reverse_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
            
        
        for i in range(left-1, right):
            reverse_vals.append(list_vals[i])

        reverse_vals.reverse()
        list_vals[left-1:right] = reverse_vals
        
        pointer = None
        head = None

        for i in range(len(list_vals)):
            if not head:
                head = ListNode(list_vals[i])
                pointer = head
            else:
                pointer.next = ListNode(list_vals[i])
                pointer = pointer.next

        return head
            
