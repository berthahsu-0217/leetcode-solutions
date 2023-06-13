# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return head
        
        node = head.next
        next_node = node.next
        node.next = head
        head.next = self.swapPairs(next_node)
        
        return node
        
        
        
        
        
        