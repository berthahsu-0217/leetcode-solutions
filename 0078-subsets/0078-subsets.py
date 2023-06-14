class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, n, arr):
            if i >= n:
                ans.append([x for x in arr])
                return
            #add nums[i]
            arr.append(nums[i])
            backtrack(i+1, n, arr)
            arr.pop()
            
            #do not add nums[i]
            backtrack(i+1, n, arr)
        
        ans = []
        backtrack(0, len(nums), [])
        
        return ans