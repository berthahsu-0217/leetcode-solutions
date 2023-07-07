class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        """
        01234567  
        TTFTTFTT
           l
               r
           i
        [2,5]
        ops 2
        """
        def slidingWindow(target):
            non_target_idx = []
            i = 0
            l = r = 0
            n = len(answerKey)
            ops = 0
            max_lens = 0
            while r < n:
                if answerKey[r] != target:
                    ops += 1
                    non_target_idx.append(r)
                if ops > k:
                    l = non_target_idx[i]+1
                    i += 1
                    ops -= 1
                max_lens = max(max_lens, r-l+1)
                r += 1
                
            return max_lens
                    
        return max(slidingWindow("T"), slidingWindow("F"))