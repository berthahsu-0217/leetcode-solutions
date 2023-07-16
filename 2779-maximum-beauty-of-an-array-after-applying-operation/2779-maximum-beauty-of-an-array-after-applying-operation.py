class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        def lowerBound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] < target:
                    l = m+1
                else:
                    r = m
            return l
        
        def upperBound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] <= target:
                    l = m+1
                else:
                    r = m
            return l
        
        n = len(nums)
        nums.sort()
        MIN = nums[0]
        MAX = nums[-1]
        
        ans = 0
        for i in range(MIN, MAX+1):
            l = lowerBound(nums, i-k)
            r = upperBound(nums, i+k)
            #print(nums[i], r, l)
            ans = max(ans, r-l)
            
        return ans
        
        
        
        