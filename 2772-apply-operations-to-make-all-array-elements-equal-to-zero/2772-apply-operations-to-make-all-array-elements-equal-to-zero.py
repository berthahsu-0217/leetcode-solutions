from collections import deque

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        """
        1. greedily turn each nonzero element to zero approached
        2. check every nonzero segments
        
        0 1 2 3 4 5
        2 3 3 3 2 2
              l
              r
    
        next_l 3
        acc 2+1-2+2
        """
        def checkSegment(i):
            if n-i < k:
                return False, i
            l = r = i
            acc = nums[l]
            next_l = deque([])
            next_l.append([l, nums[l]])
            
            while r < n:
                if nums[r]-acc < 0:
                    return False, r
                if nums[r]-acc > 0:
                    next_l.append([r, nums[r]-acc])
                    acc += nums[r]-acc
                if r-l+1 == k:
                    acc -= next_l[0][1]
                    next_l.popleft()
                    if not next_l: #every element in the segment is turned to zero
                        return True, r+1
                    else:
                        l = next_l[0][0]
                r += 1
                
            return False, n 
            
        
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
            #next segment starts with the first nonzero elements approached
            else:
                flag, i = checkSegment(i)
                if not flag:
                    return False
        return True
            
        
                
                
        