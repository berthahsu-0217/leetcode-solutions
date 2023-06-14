# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n:
            return head
            
        prev1 = None
        curr1 = head
        
        for i in range(m-1):
            prev1 = curr1
            curr1 = curr1.next
            
        prev2 = curr1
        curr2 = curr1.next
        
        for i in range(m, n):
            next_node = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = next_node
        
        curr1.next = curr2
        if prev1 is None:
            return prev2
        else:
            prev1.next = prev2
        
        return head
        
        
            
        