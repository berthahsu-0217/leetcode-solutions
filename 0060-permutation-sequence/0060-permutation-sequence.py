class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        #find the next possible digit to label at idx i
        def nextDigit(taken, last_digit = 0):
            taken[last_digit] = False
            for i in range(last_digit+1, len(taken)):
                if not taken[i]:
                    taken[i] = True
                    return i
            return -1
        
        #for every idx i, find the right digit to label
        def label(i, n, k, s, taken):
            d = nextDigit(taken)
            n_left = n-i-1
            if n_left == 0:
                return s+str(d)
            while k > n_permu[n_left]:
                k -= n_permu[n_left]
                d = nextDigit(taken, d)
            return label(i+1, n, k, s+str(d), taken)
            
        #number of permutations for i digits
        n_permu = [0 for i in range(n+1)]
        n_permu[1] = 1
        for i in range(2, n+1):
            n_permu[i] = i*n_permu[i-1]
        
        return label(0, n, k, "", [False]*(n+1))