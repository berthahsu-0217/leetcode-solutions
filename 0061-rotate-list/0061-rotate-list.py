# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        n = 0
        curr = head
        while curr is not None:
            curr = curr.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
        
        prev = None
        curr = tail = head
        cnt = 1
        while tail.next is not None:
            tail = tail.next
            if cnt >= k:
                prev = curr
                curr = curr.next
            cnt += 1
        
        assert(prev is not None)
        
        tail.next = head
        prev.next = None
        
        return curr
            
        
            
            
        