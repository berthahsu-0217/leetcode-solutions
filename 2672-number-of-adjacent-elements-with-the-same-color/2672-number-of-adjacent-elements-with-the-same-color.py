class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        nums = [0]*n
        cnt = 0
        ans = []
        
        for i, c in queries:
            if nums[i] == c:
                ans.append(cnt)
                continue
            if i+1 < n and nums[i] == nums[i+1] and nums[i] != 0:
                cnt -= 1
            if i-1 >= 0 and nums[i-1] == nums[i] and nums[i] != 0:
                cnt -= 1
            nums[i] = c
            if i+1 < n and nums[i] == nums[i+1]:
                cnt += 1
            if i-1 >= 0 and nums[i-1] == nums[i]:
                cnt += 1
            ans.append(cnt)
        
        return ans
            
        
        