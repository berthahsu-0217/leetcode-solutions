from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        max_deque = deque([]) #strictly decreasing
        min_deque = deque([]) #strictly increasing
        
        ans = 0
        n = len(nums)
        l = r = 0
        
        while r < n:
            while max_deque and max_deque[-1][0] <= nums[r]:
                max_deque.pop()
            max_deque.append([nums[r], r])
            while min_deque and min_deque[-1][0] >= nums[r]:
                min_deque.pop()
            min_deque.append([nums[r], r])
            
            while (max_deque[0][0]-min_deque[0][0]) > 2:
                l += 1
                while max_deque and max_deque[0][-1] < l:
                    max_deque.popleft()
                while min_deque and min_deque[0][-1] < l:
                    min_deque.popleft()
            ans += r-l+1
            r += 1
            
        return ans