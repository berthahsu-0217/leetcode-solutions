class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(idx, n, s, arr):
            #base case: end of candidiates or sum >= target
            if idx >= n or s >= target:
                if s == target:
                    ans.append([x for x in arr])
                return
            
            #O(n)
            for i in range(idx, n):
                arr.append(candidates[i])
                backtrack(i, n, s+candidates[i], arr)
                arr.pop()
            return
    
        ans = []
        backtrack(0, len(candidates), 0, [])
        return ans
        