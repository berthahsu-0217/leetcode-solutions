class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        val_to_max_i = dict()
        n = len(s)

        l = r = 0
        
        max_lens = 0
        while r < n:
            if s[r] in val_to_max_i:
                l = max(l, val_to_max_i[s[r]]+1)
            max_lens = max(max_lens, r-l+1)
            val_to_max_i[s[r]] = r
            r += 1
        
        return max_lens
                