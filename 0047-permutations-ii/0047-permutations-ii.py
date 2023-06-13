class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(n, arr, taken, nums, ans):
            
            if len(arr) == n:
                ans.append([x for x in arr])
                return
            
            for i in range(n):
                if not taken[i]:
                    if i > 0 and nums[i-1] == nums[i] and (not taken[i-1]):
                        continue
                    arr.append(nums[i])
                    taken[i] = True
                    dfs(n, arr, taken, nums, ans)
                    arr.pop()
                    taken[i] = False
            return
        
        n = len(nums)
        nums.sort()
        ans = []
        taken = [False for i in range(n)]
        dfs(n, [], taken, nums, ans)
        return ans