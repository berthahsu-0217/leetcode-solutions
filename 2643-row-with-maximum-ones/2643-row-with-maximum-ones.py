class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        
        max_row = 0
        max_cnt = 0
        for i in range(m):
            ones = 0
            for j in range(n):
                ones += mat[i][j]
            if max_cnt < ones:
                max_cnt = ones
                max_row = i
        
        return [max_row, max_cnt]
                