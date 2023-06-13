class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        ans = []
        n, k = len(s), len(words[0])
        
        counter = dict()
        for w in words:
            counter[w] = counter.get(w, 0)+1
        
        for i in range(k):
            memo = dict()
            l = r = i
            while r+k <= n:
                w = s[r:r+k]
                if w not in counter:
                    memo.clear()
                    l = r+k
                else:
                    memo[w] = memo.get(w,0)+1
                    while l < r and memo[w] > counter[w]:
                        memo[s[l:l+k]] -= 1
                        l += k
                    if memo == counter:
                        ans.append(l)
                r += k
        
        return ans
            
        
                        
                        
                        
                
                
                
                
                
            
        
            