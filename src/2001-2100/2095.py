# 2095. Delete the Middle Node of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        
        if not head.next:
            return None
        
        curr = head
        middle_prev = None
        middle = head
        should_skip = False
        
        while curr:
            curr = curr.next            
            
            if should_skip:
                middle_prev = middle
                middle = middle.next
                
            should_skip = not should_skip
            
        # middle is middle node, we can delete it out of the cycle
        if middle_prev and middle:
            middle_prev.next = middle.next
                    
        return head 
        