class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
        
        n = len(nums)
        ones = 0
        for x in nums:
            if x == 1: ones += 1
        if ones: return n-ones
        
        ans = float("inf")
        
        for i in range(n-1):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j-i+n-1)
                    
        if ans == float("inf"):
            return -1
        return ans
        
        
        
        