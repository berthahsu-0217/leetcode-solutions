class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        """
        Observation:
        a b c d e f g h
        
        1. k = 2
        a = c = e = g
        b = d = f = h
        
        2. k = 3
        a = d = g = b = e = h = c = f
        
        3. k = 4
        a = e 
        b = f
        c = g
        d = h
        
        => cycle length l = gcd(k, len(arr))
        => arr[i] = arr[i+l] = arr[i+2*l] = ...
        
        Take case 1 for example
        => cost(x) = abs(x-a)+abs(x-c)+abs(x-e)+abs(x-g)
        => cost(x) = abs(x-b)+abs(x-d)+abs(x-f)+abs(x-h)
        ...
        draw the function on the paper
        => minimum cost for each group is when x is medium
        """
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        n = len(arr)
        l = gcd(n, k)
        
        total_cost = 0
        
        for i in range(l):
            group = []
            for j in range(i, n, l):
                group.append(arr[j])
            group.sort()
            #print(group)
            medium = group[len(group)//2]
            for x in group:
                total_cost += abs(x-medium)
                
        return total_cost
        
        