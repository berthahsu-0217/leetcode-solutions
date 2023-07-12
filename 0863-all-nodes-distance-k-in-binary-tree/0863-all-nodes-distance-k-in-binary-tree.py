# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def dfs1(node, d, K):
            if node is None:
                return
            if d == K:
                ans.append(node.val)
                return
            dfs1(node.left, d+1, K)
            dfs1(node.right, d+1, K)
        
        def dfs2(node):
            if node is None:
                return None
            if node is target:
                return 1
            ldist = dfs2(node.left)
            if ldist is not None: #target is found in left subtree
                if K-ldist == 0: 
                    ans.append(node.val)
                elif K-ldist > 0:
                    dfs1(node.right, 1, K-ldist)
            rdist = dfs2(node.right)
            if rdist is not None:
                if K-rdist == 0:
                    ans.append(node.val)
                elif K-rdist > 0:
                    dfs1(node.left, 1, K-rdist)
            
            if ldist: return ldist+1
            if rdist: return rdist+1
            return None
            
        ans = []
        dfs1(target, 0, K)
        dfs2(root)
        return ans
        