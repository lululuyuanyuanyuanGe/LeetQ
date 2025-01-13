# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        pointer = head
        
        while pointer.next:
            length += 1
            pointer = pointer.next

        rotate_ind = length - (k % length)
        counter = 1
        end = pointer
        pointer = head
        

        while counter < rotate_ind:
            pointer = pointer.next
            counter += 1
        
        if pointer.next:
            temp_holder = pointer.next
            pointer.next = None
            end.next = head
            return temp_holder
        
        return head
        

        