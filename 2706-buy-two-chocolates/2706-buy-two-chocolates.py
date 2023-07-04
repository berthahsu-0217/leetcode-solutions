class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        min1 = None
        min2 = None
        
        for p in prices:
            if min1 is None or p <= min1:
                min2 = min1
                min1 = p
            elif min2 is None or p <= min2:
                min2 = p
        
        left = money-min1-min2
        
        return left if left >= 0 else money