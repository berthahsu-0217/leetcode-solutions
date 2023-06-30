class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        """
        1. additional edges cannot be duplicate
        
        Cases
        1. alreasy even (ok)
        
        2. add one edge => A, B are odd degrees and A, B not connected (ok)
        A <-> B   => d(A)+=1, d(B)+=1 
        
        3. add two edges with no common nodes => A,B,C,D are odd degrees and A,B not connected, C,D not connected
        A <-> B   => d(A)+=1, d(B)+=1, d(C)+=1, d(D)+=1
        C <-> D
        
        4. add two edges with a common node => C are even, A and B are odd and A,C not connected, A,B not connected
        C <-> A   => d(A)+=2, d(B)+=1, d(C)+=1
          <-> B
        """
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)
            
        odd = set()
        even = set()
        
        for i in range(n):
            if len(graph[i]) % 2:
                odd.add(i)
            else:
                even.add(i)
        
        if len(odd) == 0:
            return True
        
        if len(odd) > 4 or len(odd) % 2 == 1:
            return False

        if len(odd) == 4:
            a, b, c, d = list(odd)
            #(a,b), (c,d)
            if (a not in graph[b]) and (c not in graph[d]):
                return True
            #(a,c), (b,d)
            if (a not in graph[c]) and (b not in graph[d]):
                return True
            #(a,d), (b,c)
            if (a not in graph[d]) and (b not in graph[c]):
                return True
            return False
        
        #len(odd) == 2
        a, b = list(odd)
        if a not in graph[b]:
            return True
        
        #(a,b) are connected, find a c that is not connected to a or b
        for c in even:
            if (b not in graph[c]) and (a not in graph[c]):
                return True
            
        return False
            
        
            
            
        
        
        