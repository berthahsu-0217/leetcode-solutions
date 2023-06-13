from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        target = 0
        counter = Counter(nums)
        nums = [x for x in counter]
        nums.sort()
        ans = []
        
        for x, f in counter.items():
            if x*3 == target and f >= 3: #(x, x, x)
                ans.append([x, x, x])
            elif f >= 2 and target-2*x in counter and target-2*x != x: #(x,x,y)
                ans.append(sorted([x,x,target-2*x]))
        
        #for unique triplets
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return ans
        
        
        """
        n = len(nums)
        nums.sort()
        
        ans = []
        
        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else: #s == 0
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return ans
        """
        
        
        