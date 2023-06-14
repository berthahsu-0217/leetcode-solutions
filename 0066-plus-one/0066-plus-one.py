class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ans = []
        
        n = len(digits)
        i = n-1
        digits[-1] += 1
        carry = 0
        
        while i >= 0 or carry:
            s = carry + (0 if i < 0 else digits[i])
            carry, d = s//10, s%10
            ans.append(d)
            i -= 1
        
        return ans[::-1]
        