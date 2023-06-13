class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #TC: O(n!*n)
        #SC: O(n)
        
        def dfs(idx, n, nums, selected, arr, ans):
            
            if idx >= n:
                ans.append([x for x in arr])
                return
            
            for i in range(n):
                if not selected[i]:
                    selected[i] = True
                    arr.append(nums[i])
                    dfs(idx+1, n, nums, selected, arr, ans)
                    selected[i] = False
                    arr.pop()
                    
            return
                
        ans = []
        n = len(nums)
        dfs(0, n, nums, [False]*n, [], ans)
        return ans