class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
        ans = []
        visited = set()
        
        i = 0
        c = 1
        while True:
            visited.add(i)
            i = (i+c*k) % n
            if i in visited:
                break
            c += 1
        
        for i in range(n):
            if i not in visited:
                ans.append(i+1)
        
        return ans