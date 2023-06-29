class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        ans = 0
        #prefix_sum vertically
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j]
                
        for i in range(m):
            for j in range(i+1):
                prefix_sum = dict()
                s = 0
                for k in range(n):
                    s += matrix[i][k]-(matrix[j-1][k] if j > 0 else 0)
                    if s == target:
                        ans += 1
                    ans += prefix_sum.get(s-target,0)
                    prefix_sum[s] = prefix_sum.get(s,0)+1
        
        return ans
                    
        
                
        