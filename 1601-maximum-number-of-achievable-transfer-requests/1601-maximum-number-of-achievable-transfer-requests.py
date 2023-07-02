class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def backtrack(i, lens, dx, cnt):
            if i >= lens:
                for x in dx:
                    if x != 0: return 0
                return cnt
            
            ret = 0
            #add this request
            u, v = requests[i]
            dx[u] -= 1
            dx[v] += 1
            ret = max(ret, backtrack(i+1, lens, dx, cnt+1))
            dx[u] += 1
            dx[v] -= 1
            
            #not add this request
            ret = max(ret, backtrack(i+1, lens, dx, cnt))
            
            return ret

        dx = [0]*n
        return backtrack(0, len(requests), dx, 0)