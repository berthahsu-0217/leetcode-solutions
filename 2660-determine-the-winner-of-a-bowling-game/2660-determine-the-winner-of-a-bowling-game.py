class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def score(arr):
            sc = 0
            n = len(arr)
            for i in range(n):
                if (i-2 >= 0 and arr[i-2] == 10) or (i-1 >= 0 and arr[i-1] == 10):
                    sc += 2*arr[i]
                else:
                    sc += arr[i]

            return sc
                    
        sc1 = score(player1)
        sc2 = score(player2)
        
        #print(sc1, sc2)
        if sc1 > sc2:
            return 1
        elif sc1 == sc2:
            return 0
        else:
            return 2