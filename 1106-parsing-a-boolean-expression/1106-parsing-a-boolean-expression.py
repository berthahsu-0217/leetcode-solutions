class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        
        """
        [[t,f]]
        [&,]
        
        &(|(f,f,f,t),f)
        
        symbol & |
        """
        def eval(flag1, flag2, oper):
            if oper == "&":
                return flag1 & flag2
            else: #"|"
                return flag1 | flag2

        n = len(s)
        exp = []
        op = []
        symbol = None
        
        for i in range(n):
            if s[i] in ("!","&","|"):
                symbol = s[i]
            elif s[i] == "(":
                op.append(symbol)
                symbol = None
                exp.append(None)
            elif s[i] in ("t","f"):
                flag = True if s[i] == "t" else False
                if exp:
                    if exp[-1] is None:
                        exp[-1] = flag
                    else:
                        exp[-1] = eval(exp[-1], flag, op[-1]) 
                else:
                    exp.append(flag)
            elif s[i] == ",":
                continue
            else: #)
                oper = op.pop()
                flag = exp.pop()
                if oper == "!":
                    flag = not flag
                if exp:
                    """
                    None
                    !
                    """
                    if exp[-1] is None:
                        exp[-1] = flag
                    else:
                        exp[-1] = eval(exp[-1], flag, op[-1])
                else:
                    exp.append(flag)
            
        return exp[0]
                
                
                