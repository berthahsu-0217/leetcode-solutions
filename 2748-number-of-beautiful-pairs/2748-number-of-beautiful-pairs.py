class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
        
        ans = 0
        n = len(nums)
        
        for i in range(n-1):
            for j in range(i+1, n):
                s1 = str(nums[i])
                s2 = str(nums[j])
                a, b = int(s1[0]), int(s2[-1])
                if gcd(a, b) == 1:
                    ans += 1
        
        return ans
                