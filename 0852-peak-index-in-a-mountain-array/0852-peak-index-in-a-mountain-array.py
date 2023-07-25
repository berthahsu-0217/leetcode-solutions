class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        """
        0 1 2 3 4 5
        
        0 1 0
        0 2 1 0
        0 2 7 5 2 1
        
        
        l 0 0 2 2 
        r 6 3 3 2
        m 3 1 2 2
        """
        
        n = len(arr)
        l, r = 0, n
        
        while l < r:
            m = (l+r)//2
            #if arr[m] is last element or there is a smaller number right to it
            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m+1
        return l
        