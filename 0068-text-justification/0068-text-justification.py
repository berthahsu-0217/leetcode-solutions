class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        n = len(words)
        
        line = []
        n_char = 0
        
        for i in range(n):
            #print(words[i])
            l = len(words[i])
            #all char + all spaces + curr word
            if n_char + len(line) + l <= maxWidth:
                n_char += l
                line.append(words[i])
            else:
                if len(line) > 1:
                    n_space, left = (maxWidth-n_char)//(len(line)-1), (maxWidth-n_char)%(len(line)-1)
                else:
                    n_space, left = 0, maxWidth-n_char
                #print(n_char, line, n_space, left, maxWidth)
                s = ""
                for w in line:
                    if s != "":
                        s += " "*n_space
                        if left > 0:
                            s += " "
                            left -= 1
                    s += w
                s += " "*left
                assert(len(s) == maxWidth)
                ans.append(s)
                n_char = l
                line = [words[i]]
        
        s = ""
        for w in line:
            if s != "":
                s += " "
            s += w
        s += " "*(maxWidth-len(s))
        ans.append(s)
        
        return ans

        # ["This   is   an","example of text","justification.  "]
        # ["This    is    an","example  of text","justification.  "]
            