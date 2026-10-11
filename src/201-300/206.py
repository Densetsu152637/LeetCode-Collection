# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        next_node = head.next
        head.next = None
        return reverse_rec(head, next_node)
        
def reverse_rec(curr, next):
    if not next:
        return curr
            
    # reverse order
    next_next = next.next
    next.next = curr
    return reverse_rec(next, next_next)
    
