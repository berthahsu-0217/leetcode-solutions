# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.buildParent(None, root)
        result = []
        self.inorderTraversal2(root, result)
        return result
        
    def buildParent(self, prev, curr):
        if curr is None:
            return
        curr.parent = prev
        self.buildParent(curr, curr.left)
        self.buildParent(curr, curr.right)
        
    def inorderTraversal2(self, root, result):
    
        #left parent right
        prev = None
        curr = root

        #0: go back to parent, 1: go left, 2: print yourself and go right or parent
        while curr is not None:
            action = None
            if prev is None or prev is curr.parent:
                if curr.left is not None:
                    action = 1
                else:
                    action = 2
            elif prev is curr.left:
                action = 2
            else:
                action = 0

            prev = curr
            if action == 0:
                curr = curr.parent
            elif action == 1:
                curr = curr.left
            else:
                #print(curr.val)
                result.append(curr.val)
                if curr.right is not None: 
                    curr = curr.right
                else:
                    curr = curr.parent

