class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        """
        0^0 = 0
        0^1 = 1
        1^0 = 1
        1^1 = 0
        """
        n = len(derived)
        
        ori = [0]
        for i in range(n):
            #derived[i] = ori[i]|ord[i+1]
            if i == n-1:
                if derived[n-1] == ori[0]^ori[n-1]:
                    return True
            if derived[i] == 0:
                ori.append(0 if ori[i] == 0 else 1)
            elif derived[i] == 1:
                ori.append(0 if ori[i] == 1 else 1)
            #print(ori)
                
        ori = [1]
        for i in range(n):
            #derived[i] = ori[i]|ord[i+1]
            if i == n-1:
                if derived[n-1] == ori[0]^ori[n-1]:
                    return True
            if derived[i] == 0:
                ori.append(0 if ori[i] == 0 else 1)
            elif derived[i] == 1:
                ori.append(0 if ori[i] == 1 else 1)
        
        return False
            
            