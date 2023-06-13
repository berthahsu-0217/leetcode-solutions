class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def conquer(s1, s2):
            k = min(len(s1), len(s2))
            for i in range(k):
                if s1[i] != s2[i]:
                    return s1[:i]
            return s1[:k]
        
        def divide(l, r):
            if l+1 >= r:
                return strs[l]
            m = (l+r)//2
            s1 = divide(l, m)
            s2 = divide(m, r)
            return conquer(s1, s2)
        
        n = len(strs)
        return divide(0, n)
        