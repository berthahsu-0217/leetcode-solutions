class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        self.edges = edges
        
        critical = set()
        pseudo_critical = set()
        
        E = [[i, e[0], e[1], e[2]] for i, e in enumerate(edges)]
        E.sort(key = lambda x: x[3])
        
        min_weights, mst = self.Kruscal(n, E)
        assert(len(mst) == n-1)
        
        #check if an edge is critical, delete it and run mst
        for i in range(len(edges)):
            w_without_i, _ = self.Kruscal(n, E, i)
            if w_without_i != min_weights:
                critical.add(i)
            w_without_i, _ = self.Kruscal(n, E, connected = i)
            if w_without_i == min_weights:
                pseudo_critical.add(i)
        
        #print(critical, pseudo_critical)
        
        pseudo_critical = pseudo_critical - critical
        return list(critical), list(pseudo_critical)

    
    def find_root(self, disjoint_set, a):
        if disjoint_set[a] != a:
            disjoint_set[a] = self.find_root(disjoint_set, disjoint_set[a])
        return disjoint_set[a]
    
    def union_by_rank(self, disjoint_set, rank, a, b):
        r1 = self.find_root(disjoint_set, a)
        r2 = self.find_root(disjoint_set, b)
        if rank[r1] > rank[r2]:
            disjoint_set[r2] = r1
        elif rank[r1] < rank[r2]:
            disjoint_set[r1] = r2
        else:
            disjoint_set[r2] = r1
            rank[r1] ++ 1
        return
    
    def Kruscal(self, n, E, deleted = None, connected = None):
                
        disjoint_set, rank = [i for i in range(n)], [1]*n
        mst = []
        weights = 0
        
        if connected is not None:
            mst.append(connected)
            weights += self.edges[connected][2]
            self.union_by_rank(disjoint_set, rank, self.edges[connected][0], self.edges[connected][1])
        
        for i, a, b, w in E:
            
            #if this edge is deleted, skip it
            if i == deleted: continue
                
            #if a and b not connected, use this edge to connect them
            if self.find_root(disjoint_set, a) != self.find_root(disjoint_set, b):
                mst.append(i)
                weights += w
                self.union_by_rank(disjoint_set, rank, a, b)
        
        return weights, mst
            
                
                
                
        
        

        
        
        
        
        
        