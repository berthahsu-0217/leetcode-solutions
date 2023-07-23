# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n % 2 == 0:
            return []
        
        def serialize(k):
            if k == 1:
                return ["(0)"]
            arr = []
            for i in range(1,k,2):
                larr = serialize(i)
                rarr = serialize(k-1-i)
                for s1 in larr:
                    for s2 in rarr:
                        arr.append("(0"+s1+s2+")")
            return arr
            
        trees = serialize(n)
        
        def deserialize(s, i):
            
            #(0
            i += 2
            node = TreeNode()
            #subtree
            """
            (0(0(0(0)(0))(0))(0))
                           i  
            """
            if s[i] == ")":
                return node, i+1
            elif s[i] == "(":
                node.left, i = deserialize(s, i)
                if s[i] == "(":
                    node.right, i = deserialize(s, i)
            if s[i] == ")":
                i += 1
            return node, i
        
        #buildTree("(0(0(0(0)(0))(0))(0))", 0)
        #return
        #print(trees)
        
        ans = []    
        for s in trees:
            #print(s)
            root = deserialize(s, 0)[0]
            ans.append(root)
        return ans
            
            

        