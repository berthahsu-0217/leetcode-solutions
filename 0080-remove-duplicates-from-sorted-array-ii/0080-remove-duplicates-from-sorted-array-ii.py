class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 1:
            return 1
        
        empty = None
        
        cnt = 1
        
        #[0,0,1,1,2,3,3,3,3]
   #cnt   1 2 1 2 3 4 1 1 2
   #empty N N N N 4 4 5 6 7
    
        #[1,1,2,2,3,3]
   #cnt   1 2 3 1 2 1
   #empty N N 2 3 4 5

        for i in range(1,n):
        
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt <= 2 and empty is not None:
                nums[empty] = nums[i]
                empty += 1
                      
            if cnt > 2 and empty is None:
                empty = i
        
        if empty is None:
            return n
        else:
            return empty