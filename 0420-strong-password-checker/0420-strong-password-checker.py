class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        """
        1. It is always least expensive to use replacements instead of adding/deleting
        2. If n < 6: mandatory adding = (6-n)
        3. If n > 20: mandatory deleteing = (n-20)
        4. See how many required replacements can be substituted by adding and deleting
        5. count the remaining required replacements
        6. if (add+replacement) < required: count additional adding for 2nd conditions
        
        n//3: number of replacements required at least
        
        n%3 == 0
        aaa: aax, aaba, aab
        aaaaaa: aabaax, aabaabaa, aabaab
        aaaaaaaaa: aabaabxx,     , aabaabaab
        => 1 replace = 1 add = 1 delete 
        
        n%3 == 1
        aaaa: aaxx, aabaa, aaba
        aaaaaaa: aabaaxx, aabaabaa, aabaaba
        => 1 replace = 1 add = 2 delete
        
        n%3 == 2
        aaaaa: aaxxx, aabaaba, aabaa
        aaaaaaaa: aabaaxxx, aabaabaaba
        => 1 replace = 2 add = 3 delete
        """
        
        n = len(password)
        
        lowercase = uppercase = digit = True
        for c in password:
            if ord("a") <= ord(c) <= ord("z"):
                lowercase = False
            elif ord("A") <= ord(c) <= ord("Z"):
                uppercase = False
            elif c.isdigit():
                digit = False
        missing = int(lowercase)+int(uppercase)+int(digit)
        
        changes = 0
        zero_remainder = 0
        one_remainder = 0
        
        cnt = 0
        for i in range(n+1):
            if i == n or (i > 0 and password[i-1] != password[i]):
                if cnt >= 3:
                    changes += cnt//3
                    if cnt % 3 == 0: zero_remainder += 1
                    if cnt % 3 == 1: one_remainder += 1
                cnt = 0
            cnt += 1
            
        #print(changes)
        
        if n < 6:
            return max(missing, 6-n)
        elif n <= 20:
            return max(missing, changes)
        else:
            deletes = n - 20
            
            changes -= min(deletes, zero_remainder)
            changes -= min(max(deletes-zero_remainder, 0), one_remainder*2) // 2
            changes -= max(deletes-zero_remainder-2*one_remainder, 0) // 3
                
            return deletes + max(missing, changes)
                
        
        
        
        
        
                    
                    
                
                
        