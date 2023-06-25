class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        held, sold = float("-inf"), 0
        
        for p in prices:
            #buy at p
            h = max(held, sold-p-fee)
            #sell at p
            s = max(sold, held+p)
            #do nothing
            
            held, sold = h, s
            
        return sold