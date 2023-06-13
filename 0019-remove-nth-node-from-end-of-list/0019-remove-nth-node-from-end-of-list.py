# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = tail = head
        cnt = 1
        
        while tail.next:
            tail = tail.next
            if cnt == n:
                prev = curr
                curr = curr.next
            else:
                cnt += 1
        
        if not prev:
            return curr.next
        prev.next = curr.next
        return head
        
        