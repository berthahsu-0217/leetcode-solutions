class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        """
        maintain the relative order of each tree
        """
        def combi(n, k):
            if k < n-k:
                return combi(n, n-k)
            a = b = 1
            for i in range(k+1, n+1):
                a *= i
            for i in range(2, n-k+1):
                b *= i
            return a//b
        
        def dfs(arr):
            n = len(arr)
            if n < 3: return 1
            lt = []
            gt = []
            for x in arr:
                if x < arr[0]:
                    lt.append(x)
                elif x > arr[0]:
                    gt.append(x)
            
            return dfs(lt)*dfs(gt)*combi(n-1, len(lt)) % MOD
        
        MOD = 1000000007
        return (dfs(nums)-1) % MOD
        