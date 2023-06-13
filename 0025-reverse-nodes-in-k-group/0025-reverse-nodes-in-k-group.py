# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #old_head, old tail: return new_head, new_tail
        def reverse(old_head):
            """
            n <- 1 <- 2
                
            next_node n
            prev 2
            curr n
            """
            prev = None
            curr = old_head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, old_head #new_head, new_tail
        
        
        if head is None:
            return None
        
        tail = head
        for i in range(k-1):
            tail = tail.next
            if tail is None:
                return head
            
        next_head = tail.next
        tail.next = None
        
        new_head, new_tail = reverse(head)
        new_tail.next = self.reverseKGroup(next_head, k)
        return new_head
        
        