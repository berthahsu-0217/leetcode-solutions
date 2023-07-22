import queue

class Solution:
    def knightProbability(self, N: int, k: int, r: int, c: int) -> float:
        
        q = queue.Queue()
        q.put((r,c,k))
        explored = dict()
        explored[(r,c,k)] = 1
        
        dx = [-2,-1,-2,-1,2,1,2,1]
        dy = [-1,-2,1,2,-1,-2,1,2]
        
        cnt = 0
        while not q.empty():
            x, y, s = q.get()
            if s == 0:
                cnt += explored[(x,y,s)]
                continue
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                    if (new_x,new_y,s-1) not in explored:
                        q.put((new_x, new_y, s-1))
                        explored[(new_x,new_y,s-1)] = explored[(x,y,s)]
                    else:
                        explored[(new_x,new_y,s-1)] += explored[(x,y,s)]
                        
        return float(cnt)/float(8**k)