class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        """
        1. Break the elements in A and B into L and R, where all elements in L <= all elements in R
        2. Assuming m = len(A), n = len(B), we want to find index 0 <= i < m in A and index 0 <= j < n in B, such that:
            a) m <= n 
            b) if m+n is even ==> i+j = m-i+n-j => len(L) = len(R)
               if m+n is odd ==> i+j = m-i+n-j+1 => len(L) = len(R)+1
            c) A[i-1] <= B[j]
            d) B[j-1] <= A[i]
        3. Binary search for i ==> j = (m+n+1)//2-i ==> so that's why we must ensure m <= n
            a) if i > 0 and j < n and A[i-1] > B[j] ==> decrease i
            b) if j > 0 and i < m and B[j-1] > A[i] ==> increase i
            c) else: (i=0 or j=n or A[i-1] <= B[j]) and (j=0 or i=m or B[j-1] <= A[i]) ==> stop search
               if m+n is even ==> (L_max+R_min)/2
               if m+n is odd ==> L_max
        """
        
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        m, n = len(A), len(B)
        l, r = 0, m
        L_max = R_min = None
        
        while l <= r:
            i = (l+r)//2
            j = (m+n+1)//2-i
            
            if i > 0 and j < n and A[i-1] > B[j]:
                r = i
            elif j > 0 and i < m and B[j-1] > A[i]:
                l = i+1
            else:
                if i > 0:
                    L_max = A[i-1]
                if L_max is None or (j > 0 and B[j-1] > L_max):
                    L_max = B[j-1]
            
                if (m+n) % 2 == 1:
                    return L_max
                
                if i < m:
                    R_min = A[i]
                if R_min is None or (j < n and B[j] < R_min):
                    R_min = B[j]
                                       
                return (L_max+R_min)/2
                    
                    
            
            