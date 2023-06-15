# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        max_sum = float("-inf")
        
        q = queue.Queue()
        if root:
            q.put(root)
        
        lv = 1
        while not q.empty():
            s = 0
            for i in range(q.qsize()):
                node = q.get()
                s += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if s > max_sum:
                max_sum = s
                ans = lv
            lv += 1
        
        return ans
            