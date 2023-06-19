class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        max_alt = 0
        alt = 0
        
        for d in gain:
            alt += d
            max_alt = max(max_alt, alt)
        
        return max_alt