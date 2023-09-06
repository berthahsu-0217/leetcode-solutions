# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        lens, r = divmod(n,k)
        
        ans = []
        curr = head
        
        for i in range(k):
            if not curr:
                ans.append(None)
                continue
            ans.append(curr)
            m = lens
            if r > 0:
                m += 1
                r -= 1
            for j in range(m-1):
                curr = curr.next
            next_node = curr.next
            curr.next = None
            curr = next_node

        return ans
                
            
            
        