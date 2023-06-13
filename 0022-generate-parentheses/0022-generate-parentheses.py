class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol = []
        
        def backtrack(lcnt, rcnt, arr):
            if len(arr) == 2*n:
                sol.append("".join(arr))
                return
            if lcnt < n:
                arr.append('(')
                backtrack(lcnt+1, rcnt, arr)
                arr.pop()
            if rcnt < lcnt:
                arr.append(')')
                backtrack(lcnt, rcnt+1, arr)
                arr.pop()
        
        backtrack(0, 0, [])
        #print(sol)
        return sol