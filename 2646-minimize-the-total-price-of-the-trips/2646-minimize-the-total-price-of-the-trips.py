class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        """
        0,3 => 0,1,3
        2,1 => 2,1
        2,3 => 2,1,3
        
        [1,3,2,2]
        """
        #O(N+E)
        def dfs(node, parent, target):
            if node is target:
                freq[node] += 1
                return True
            for child in tree[node]:
                if child != parent:
                    if dfs(child, node, target):
                        freq[node] += 1
                        return True
            return False
        
        @cache
        def dfs1(node, parent, halved):
            curr_cost = (price[node]//2 if halved else price[node])*freq[node]
            subtree_cost = 0
            
            for child in tree[node]:
                if child != parent:
                    cost = dfs1(child, node, False)
                    if not halved:
                        cost = min(cost, dfs1(child, node, True))
                    subtree_cost += cost
            
            return curr_cost+subtree_cost
            
                
        tree = [set() for i in range(n)]
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        
        freq = [0]*n
        for start, end in trips:
            dfs(start, -1, end)
            
        #print(freq)
        min_cost = min(dfs1(0,-1,True), dfs1(0,-1,False))
        
        return min_cost
        
        
            
        
            
            
        
            
        
        