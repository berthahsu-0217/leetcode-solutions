class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = [] #instrictly increasing
        
        i = 0
        n = len(heights)
        while i < n or stack:
            height = width = 0
            while stack and (i == n or stack[-1][0] > heights[i]):
                hh, ww = stack.pop()
                height = hh
                width += ww
                max_area = max(max_area, height*width)
            if i < n:
                stack.append([heights[i], width+1])
                i += 1
        
        return max_area
            
        