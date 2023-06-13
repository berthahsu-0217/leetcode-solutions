# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                hq.heappush(heap, (lists[i].val, i, lists[i]))
        
        head = None
        curr = head
        
        while heap:
            val, idx, node = hq.heappop(heap)
            if head is None:
                head = curr = node
            else:
                curr.next = node
                curr = curr.next
            if node.next:
                node = node.next
                hq.heappush(heap, (node.val, idx, node))
        
        return head