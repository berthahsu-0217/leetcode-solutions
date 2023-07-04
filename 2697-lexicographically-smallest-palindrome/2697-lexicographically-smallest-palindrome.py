class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        arr = [c for c in s]
        
        n = len(s)
        
        l, r = 0, n-1
        
        while l < r:
            if arr[l] != arr[r]:
                if ord(arr[l]) <= ord(arr[r]):
                    arr[r] = arr[l]
                else:
                    arr[l] = arr[r]
            l += 1
            r -= 1
        
        return "".join(arr)
            