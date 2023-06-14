# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inorder(node):
            
            if node is None: 
                return
            
            inorder(node.left)
            if self.prev:
                self.min_diff = min(self.min_diff, node.val-self.prev.val)
            self.prev = node
            inorder(node.right)
        
        self.min_diff = float("inf")
        self.prev = None
        inorder(root)
        return self.min_diff
            