class Solution:
    def countAndSay(self, n: int) -> str:
        
        def read(digits):
            s = ""
            cnt = 0
            d = ""
            for x in digits:
                if x != d:
                    if d != "":
                        s += str(cnt)+str(d)
                    cnt = 0
                d = x
                cnt += 1
            if d != "":
                s += str(cnt)+str(d)
            return s
        
        digits = "1"
        for i in range(n-1):
            digits = read(digits)
            
        return digits
        

        
        
        
        
        
        