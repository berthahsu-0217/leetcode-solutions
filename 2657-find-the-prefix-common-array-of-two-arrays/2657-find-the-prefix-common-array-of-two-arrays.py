class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        ans = [0]*n
        
        setA = set()
        setB = set()
        
        cnt = 0
        for i in range(n):
            if A[i] == B[i]:
                cnt += 1
            if A[i] in setB:
                cnt += 1
            if B[i] in setA:
                cnt += 1
            ans[i] = cnt
            setA.add(A[i])
            setB.add(B[i])
        
        return ans
            