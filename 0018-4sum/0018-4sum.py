class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def pair(l, r, a, b, target, arr, ans):
            goal = target-a-b
            while l < r:
                if arr[l]+arr[r] == goal:
                    ans.append([a,b,arr[l],arr[r]])
                    l += 1
                    r -= 1
                elif arr[l]+arr[r] > goal:
                    r -= 1
                else:
                    l += 1
            return
        
        ans = []
        char_to_freq = dict()
        for c in nums:
            char_to_freq[c] = char_to_freq.get(c,0)+1
        arr = [c for c in char_to_freq]
        arr.sort()
        
        n = len(arr)
        
        #all distinct
        for i in range(n-3):
            for j in range(i+1, n-2):
                pair(j+1, n-1, arr[i], arr[j], target, arr, ans)
                
        #two same, two distinct
        for i in range(n):
            if char_to_freq[arr[i]] < 2:
                continue
            for j in range(n-1):
                if j == i:
                    continue
                for k in range(j+1, n):
                    if k == i:
                        continue
                    if arr[i]*2+arr[j]+arr[k] == target:
                        ans.append([arr[i], arr[i], arr[j], arr[k]])
        
        #two same, two same
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i]*2+arr[j]*2 == target and char_to_freq[arr[i]] >= 2 and char_to_freq[arr[j]] >= 2:
                    ans.append([arr[i], arr[i], arr[j], arr[j]])
                    
        #three same
        for i in range(n):
            if char_to_freq[arr[i]] < 3:
                continue
            for j in range(n):
                if i == j:
                    continue
                if arr[i]*3+arr[j] == target:
                    ans.append([arr[i], arr[i], arr[i], arr[j]])
                    
                    
        #four same
        for i in range(n):
            if arr[i]*4 == target and char_to_freq[arr[i]] >= 4:
                ans.append([arr[i], arr[i], arr[i], arr[i]])
        
        return ans