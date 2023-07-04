class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        
        """
        even palindrome: must have a palindrome of length 2
        odd palindrome: must have a palindrome of length 3
        """
        n = len(s)
        A = [ord(c)-ord('a') for c in s]
        
        i = n-1
        A[i] += 1
        while i >= 0:
            if A[i] == k:
                i -= 1
            elif A[i] not in A[max(i-2, 0):i]: #string is larger and beautiful
                break
            A[i] += 1
        
        if i < 0: return ""
        
        #print(A)
        for j in range(i+1, n): #make all k to 1 or 2 or 3
            A[j] = min({0, 1, 2} - set(A[max(j-2, 0): j]))
            
        return "".join(chr(ord('a') + a) for a in A)
            
            
            
                
                
            
            