# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        return self.solution1(root)
        
    def solution1(self, root):
        
        def inorder(node):
            if node is None: return
            inorder(node.left)
            sorted_tree.append(node.val)
            inorder(node.right)
        
        sorted_tree = []
        inorder(root)
        #print(sorted_tree)
        ans = float("inf")
        for i in range(1, len(sorted_tree)):
            ans = min(ans, sorted_tree[i]-sorted_tree[i-1])
        return ans
            