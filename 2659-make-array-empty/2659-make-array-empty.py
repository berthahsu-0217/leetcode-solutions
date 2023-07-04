class Solution:
    def countOperationsToEmptyArray(self, A: List[int]) -> int:
        
        """
        0 1 2 3 4 5 6 7 8
        7 8 9 1 2 4 5 6 3
        
        7 8 9 4 5 6
        
        1 2 3 4 5 6 7 8 9
        """
        pos = {a: i for i, a in enumerate(A)}
        res = n = len(A) #at least n operations
        A.sort()
        for i in range(1, n):
            #elements in strictly increasing order are removed at this round
            if pos[A[i]] < pos[A[i-1]]: 
                res += n - i #additional rotations at this round = number of remaing elements
        return res
                
        