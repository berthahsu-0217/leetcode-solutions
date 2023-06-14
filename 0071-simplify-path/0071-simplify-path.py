class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        i, n = 0, len(path)
        
        while i < n and path[i] == "/":
            i += 1
        
        while i < n:
            file = ""
            while i < n and path[i] != "/":
                file += path[i]
                i += 1
                
            if file == "..":
                if stack: stack.pop()
            elif file != "." and file != "":
                stack.append(file)
            
            while i < n and path[i] == "/":
                i += 1
        
        #print(stack)
        ans = "/"+"/".join(stack)
        return ans
                
            
            
            
            