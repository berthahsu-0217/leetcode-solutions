# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        if n == 0:
            return []
        
        return self.construct(1, n+1)
        
    def construct(self, start, end):
        
        ans = []
        
        if start+1 == end:
            return [TreeNode(start)]
        if start == end:
            return [None]
        
        for i in range(start, end):
            l_arr = self.construct(start, i)
            r_arr = self.construct(i+1, end)
            
            for l_node in l_arr:
                for r_node in r_arr:
                    node = TreeNode(i)
                    node.left = l_node
                    node.right = r_node
                    ans.append(node)
                    
        return ans