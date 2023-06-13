class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans = float("inf")
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if abs(s-target) < abs(ans-target):
                    ans = s
                if s == target:
                    return target
                elif s > target:
                    r -= 1
                else: #s < target
                    l += 1
        return ans