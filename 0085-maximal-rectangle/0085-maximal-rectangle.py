class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def maxRecArea(heights):
            
            #strictly increasing
            stack = []
            max_area = 0
            
            for h in heights:
                width = 0
                while len(stack) > 0 and stack[-1][0] > h:
                    hh, ww = stack.pop()
                    width += ww
                    max_area = max(max_area, hh*width)
                stack.append([h, width+1])
            
            width = 0
            while len(stack) > 0:
                hh, ww = stack.pop()
                width += ww
                max_area = max(max_area, hh*width)
            
            return max_area
                  
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for j in range(n):
            ones = 0
            for i in range(m):
                if matrix[i][j] == "0":
                    ones = 0
                else:
                    ones += 1
                dp[i][j] = ones
                
        max_area = 0
        for i in range(m):
            max_area = max(max_area, maxRecArea(dp[i]))
        return max_area