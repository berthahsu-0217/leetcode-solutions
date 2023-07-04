class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single = 0
        
        power = 1
        for i in range(32):
            freq = 0
            for x in nums:
                if x & power != 0:
                    freq += 1
            if freq % 3:
                single |= 1 << i
            power <<= 1
            
        return single if single < (1 << 31) else single- (1 << 32)
        
        
        
        