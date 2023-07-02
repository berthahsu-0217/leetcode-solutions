class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        """
             3 2 5 4
        odd  0 0 2 0
        even 0 1 0 3
        """
        max_len = 0
        odd = even = 0
        
        for x in nums:
            if x > threshold:
                odd = even = 0
            elif x % 2 == 0: #even
                even = odd+1
                odd = 0
            else: #odd
                odd = even+1 if even > 0 else 0
                even = 0
            #print(odd, even)
            max_len = max(max_len, even, odd)
        
        return max_len
                
        
        