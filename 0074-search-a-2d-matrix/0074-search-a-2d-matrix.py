class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        row_idx = self.lowerBoundRow(0, m, n-1, matrix, target)
        if row_idx >= m:
            return False
        col_idx = self.lowerBoundCol(0, n, row_idx, matrix, target)
        return col_idx < n and matrix[row_idx][col_idx] == target
    
    def lowerBoundRow(self, l, r, col_idx, matrix, target):
        
        while l < r:
            mid = (l+r)//2
            if matrix[mid][col_idx] < target:
                l = mid+1
            else:
                r = mid
                
        return l
        
    def lowerBoundCol(self, l, r, row_idx, matrix, target):
        
        while l < r:
            mid = (l+r)//2
            if matrix[row_idx][mid] < target:
                l = mid+1
            else:
                r = mid
                
        return l
        
        
        