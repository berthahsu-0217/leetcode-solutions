# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        interval = [-float("inf"), float("inf")]
        
        return self.check(root, interval)
        
    def check(self, node, interval):
        
        if node is None:
            return True
        
        lcheck = self.check(node.left, [interval[0], node.val])
        rcheck = self.check(node.right, [node.val, interval[1]])
        
        ccheck = False
        if interval[0] < node.val and node.val < interval[1]:
            ccheck = True
            
        return ccheck and lcheck and rcheck
        
        