class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        max_lens = 0
        n = len(s)
        left = right = 0
        for i in range(n):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1
            if left == right:
                max_lens = max(max_lens, 2*right)
            elif left < right:
                left = right = 0
        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1
            if left == right:
                max_lens = max(max_lens, 2*left)
            elif left > right:
                left = right = 0
                
        return max_lens