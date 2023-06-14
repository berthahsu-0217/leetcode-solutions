class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        self.recurse(k, 1, n+1, [], ans)
        return ans
    
    def recurse(self, k, start, n, curr, ans):
        
        if len(curr) == k:
            ans.append([x for x in curr])
            return
        
        for i in range(start, n):
            curr.append(i)
            self.recurse(k, i+1, n, curr, ans)
            curr.pop()
            
        return