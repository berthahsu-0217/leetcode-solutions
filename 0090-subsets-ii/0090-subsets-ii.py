class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, n, arr):
            
            if i >= n:
                ans.append([x for x in arr])
                return
            
            #add nums[i]
            arr.append(nums[i])
            backtrack(i+1, n, arr)
            arr.pop()
            
            #not add nums[i]
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, n, arr)
            
        nums.sort()
        ans = []
        backtrack(0, len(nums), [])
        return ans