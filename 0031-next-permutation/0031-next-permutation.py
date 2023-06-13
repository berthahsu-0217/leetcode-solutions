class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def reverse(idx, n, nums):
            l, r = idx, n-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return
        
        def findJustLarger(val, idx, n, nums):
            for i in range(idx, n):
                if i == n-1 or (nums[i] > val and nums[i+1] <= val):
                    return i
            return -1
        
        n = len(nums)
        i = n-1
        while i > 0:
            if nums[i-1] < nums[i]:
                j = findJustLarger(nums[i-1], i, n, nums)
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
            i -= 1
            
        reverse(i, n, nums)
        
        return
        

            