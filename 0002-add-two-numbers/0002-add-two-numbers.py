# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(-1)
        curr = dummyHead
        
        carry = 0
        """
        1. whether there is still elements in l1 or l2
        2. if carry > 0, append an extra node to tail
        """
        #O(max(n1, n2))
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1+val2+carry
            d, carry = s%10, s//10
            node = ListNode(d)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyHead.next
            