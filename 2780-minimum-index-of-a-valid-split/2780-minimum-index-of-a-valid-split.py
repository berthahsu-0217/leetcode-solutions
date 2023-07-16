class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_element1 = [None]*n
        max_element2 = [None]*n
        
        dominant = None
        max_f = 0
        counter = dict()
        
        for i in range(n):
            x = nums[i]
            counter[x] = counter.get(x,0)+1
            if counter[x] > max_f:
                max_f = counter[x]
                dominant = x
            max_element1[i] = [dominant, max_f]
            
        dominant = None
        max_f = 0
        counter = dict()
            
        for i in range(n-1,-1,-1):
            x = nums[i]
            counter[x] = counter.get(x,0)+1
            if counter[x] > max_f:
                max_f = counter[x]
                dominant = x
            max_element2[i] = [dominant, max_f]
            
        #print(max_element1)
        #rint(max_element2)
        
        for i in range(n):
            #print(i+1, n-i-1)
            if 0 <= i < n-1 and max_element1[i][0] == max_element2[i+1][0] == dominant and max_element1[i][1]*2 > i+1 and max_element2[i+1][1]*2 > n-i-1:
                return i
        
        return -1
            
        
        
        