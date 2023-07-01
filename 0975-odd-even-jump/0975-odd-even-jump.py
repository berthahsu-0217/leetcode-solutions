class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        """
        Reference: https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
        
        0 1 2 3 4
        5,1,3,4,2
        
        higher(2) = T
        lower(2) = T
        
        higher(4) = F
        lower(4) = 
        
                         j
        (1,1)(2,4)(3,2)(4,3)(5,0)
        stack = [4,3,0]
        next_higher [0,1,3,0,0]
        
        (5,0)(4,3)(3,2)(2,4)(1,1)
        stack = [1]
        next_lower  [3,0,4,4,0]
        
        higher = [F,F,F,F,T]
        lower = [F,F,F,F,T]
        """
        n = len(arr)
        next_higher, next_lower = [0]*n, [0]*n
        
        val_and_idx = [(val, idx) for idx, val in enumerate(arr)]
        
        stack = [] #decreasing
        val_and_idx.sort()
        for x, i in val_and_idx:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
            
        stack = []
        val_and_idx.sort(key = lambda x: (-x[0], x[1]))
        for x, i in val_and_idx:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
            
        higher, lower = [0]*n, [0]*n
        higher[-1] = lower[-1] = True
        for i in range(n-2,-1,-1):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
        