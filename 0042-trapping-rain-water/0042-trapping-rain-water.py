class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        stack = []
        n = len(height)
        
        for i in range(n):
            right_h = 0 
            while stack and stack[-1][0] <= height[i]:
                h, idx = stack.pop()
                water += (h-right_h)*(i-idx-1)
                right_h = h
            if stack:
                h, idx = stack[-1]
                water += (height[i]-right_h)*(i-idx-1)
            stack.append([height[i], i])
        
        return water
        