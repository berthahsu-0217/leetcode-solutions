class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(idx, n, letters, s, sol):
            #end of string
            if idx >= n:
                sol.append(s)
                return
            for c in letters[int(digits[idx])]:
                dfs(idx+1, n, letters, s+c, sol)
            return
        
        #special case: empty string
        if digits == "":
            return []
        
        sol = []
        letters = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        dfs(0, len(digits), letters, "", sol)
        
        return sol