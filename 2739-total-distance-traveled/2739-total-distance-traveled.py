class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
        ans = 0
        
        while mainTank >= 5:
            ans += 5*10
            mainTank -= 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        
        ans += mainTank*10
        
        return ans
            