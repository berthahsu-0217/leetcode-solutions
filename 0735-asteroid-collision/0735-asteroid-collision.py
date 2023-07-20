class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for x in asteroids:
            add = True
            while len(stack) > 0 and stack[-1] > 0 and x < 0:
                if stack[-1] >= abs(x):
                    if stack[-1] == abs(x):
                        stack.pop()
                    add = False
                    break
                stack.pop()
            if add:
                stack.append(x)
            
        return stack
    
            