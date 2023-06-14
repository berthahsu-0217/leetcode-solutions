# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        memo = dict()
        
        prev = None
        curr = head

        
        while curr is not None:
            if curr.val in memo:
                prev = memo[curr.val]
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                memo[curr.val] = prev
                prev = curr
            curr = curr.next
            
        return head