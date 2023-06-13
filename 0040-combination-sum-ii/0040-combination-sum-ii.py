class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(idx, n, candidates, s, target, arr, ans):
            if s == target:
                ans.append([x for x in arr])
                return
            if idx >= n or s > target:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                arr.append(candidates[i])
                dfs(i+1, n, candidates, s+candidates[i], target, arr, ans)
                arr.pop()
            return
        
        candidates.sort()
        ans = []
        dfs(0, len(candidates), candidates, 0, target, [], ans)
        return ans