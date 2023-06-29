class Solution:
    def isValid(self, code: str) -> bool:
        
        """
        1. valid closed tag
        2. valid tag name: uppercase, length [1,9]
        3. valid tag content: valid closed tags, cdata
        4. if there is a < or </, find >
        """
        
        """
        For a valid CDATA
        1. must start with "<![CDATA[" and end with "]]>"
        2. total length >= 12
        """
        def isTagContent(i, n):
            
            while i < n:
                if i+1 < n and code[i:i+2] == "<!":
                    flag, idx = isCDATA(i, n)
                    if not flag:
                        return False, -1
                    i = idx
                elif i+1 < n and code[i:i+2] == "</":
                    return True, i
                elif i+1 < n and code[i] == "<":
                    print("this", code[i:])
                    flag, idx = isClosed(i, n)
                    if not flag:
                        return False, -1
                    i = idx
                else:
                    i += 1
            return True, i
        
        def isCDATA(i, n):
            if i+12 > n or code[i:i+9] != "<![CDATA[":
                return False, -1
            i += 9
            while i+3 <= n and code[i:i+3] != "]]>":
                i += 1
            if i+3 > n or code[i:i+3] != "]]>":
                return False, -1
            i += 3
            return True, i
                
        def isStartTag(i, n):
            if i+3 > n or code[i] != "<":
                return False, -1, ""
            i += 1
            tag_name = ""
            while i < n and code[i] != ">":
                if not (code[i].isalpha() and code[i].isupper()):
                    return False, -1, ""
                tag_name += code[i]
                i += 1
            if i >= n or code[i] != ">" or len(tag_name) > 9 or len(tag_name) == 0:
                return False, -1, ""
            i += 1
            return True, i, tag_name
        
        def isEndTag(i, n):
            if i+4 > n or code[i:i+2] != "</":
                return False, -1, ""
            i += 2
            tag_name = ""
            while i < n and code[i] != ">":
                if not (code[i].isalpha() and code[i].isupper()):
                    return False, -1, ""
                tag_name += code[i]
                i += 1
            if i >= n or code[i] != ">" or len(tag_name) > 9 or len(tag_name) == 0:
                return False, -1, ""
            i += 1
            return True, i, tag_name
        
        def isClosed(i, n):
            flag, i, start_tag = isStartTag(i, n)
            if not flag:
                print("start tag wrong")
                return False, -1
            print(code[i:])
            flag, i = isTagContent(i, n)
            if not flag:
                print("tag content wrong")
                return False, -1
            print(code[i:])
            flag, i, end_tag = isEndTag(i, n)
            if (not flag) or (start_tag != end_tag):
                print("end tag wrong")
                return False, -1
            return True, i
        
        n = len(code)
        return isClosed(0, n)[1] == n
        
        """
        test = ["<DIV>","<>","<A>","<A1>","<AB","<ABCDEFGHIJK>","A>"]
        for t in test:
            code = t
            print(isStartTag(0, len(code)))
        """
        """
        test = ["</DIV>","</>","</A>","</A1>","<AB/","</ABCDEFGHI>","<"]
        for t in test:
            code = t
            print(isEndTag(0, len(code)))
        """
        """
        "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
        """
        
        
            
                    
                
            
        
        
        