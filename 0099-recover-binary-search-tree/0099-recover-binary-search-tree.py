# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        arr = []
        self.inorder(root, arr)
        
        wrong_idx = None
        for i in range(len(arr)-1):
            if arr[i].val > arr[i+1].val:
                wrong_idx = i
                break
        
        wrong_idx2 = None
        for i in range(wrong_idx+1, len(arr)):
            if arr[i].val > arr[wrong_idx].val:
                wrong_idx2 = i-1
                break
        
        if wrong_idx2 is None:
            wrong_idx2 = len(arr)-1
            
        arr[wrong_idx].val, arr[wrong_idx2].val = arr[wrong_idx2].val, arr[wrong_idx].val
        
        return

    def inorder(self, node, arr):
        
        if node is None:
            return
        
        self.inorder(node.left, arr)
        arr.append(node)
        self.inorder(node.right, arr)