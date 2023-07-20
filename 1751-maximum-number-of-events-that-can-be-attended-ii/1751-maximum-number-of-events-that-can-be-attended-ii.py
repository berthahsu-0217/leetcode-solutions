class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        """
        TC: n*(k+logn)
        1. sort => O(n*logn)
        2. backtrack: n*k
        3. binarySearch: n*logn 
        """
        
        @cache
        def binarySearch(last_end):
            l, r = 0, len(events)
            while l < r:
                m = (l+r)//2
                if events[m][0] <= last_end:
                    l += 1
                else:
                    r = m
            return l
        
        @cache
        def backtrack(last_end, tickets):
            if tickets == 0:
                return 0
            max_sum = 0
            l = binarySearch(last_end)
            for i in range(l, n):
                max_sum = max(max_sum, events[i][2]+backtrack(events[i][1], tickets-1))
            return max_sum
        
        n = len(events)
        events.sort()
        return backtrack(0, k)