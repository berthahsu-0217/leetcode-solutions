# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        new_head_one = new_head_two = None
        prev_one = prev_two = None
        
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = None
            if curr.val < x:
                if new_head_one is None:
                    new_head_one = curr
                else:
                    prev_one.next = curr
                prev_one = curr
            else:
                if new_head_two is None:
                    new_head_two = curr
                else:
                    prev_two.next = curr
                prev_two = curr
            curr = nextNode
        
        """
        self.print(new_head_one)
        print("---")
        self.print(new_head_two)
        
        print(prev_one.val, prev_two.val)
        """
        
        if prev_one is not None:
            prev_one.next = None
        if prev_two is not None:
            prev_two.next = None
            
        if new_head_one is not None:
            prev_one.next = new_head_two
            return new_head_one
        else:
            return new_head_two
    
    def print(self, node):
        
        while node is not None:
            print(node.val)
            node = node.next
            
        return
            