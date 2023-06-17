class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
       
        """
        1. There is a best option for replacing each element
           => the smallest number that is just bigger than the previous element
           => sort arr2, and use binary search to find that best option
        
        2. For each level i of iteration, update a dp dictionary,
           where dp[num]: min number of operations to make 0~i elements
           strictly increasing when arr1[i] = num
        
        3. Updating dp:
           3.1 Iterate every possible dp[num] from the previous index
               => replace, then find the best option to replace it
               => no replace, then arr1[i] must be bigger than num
        """
        def upperBound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] <= target:
                    l = m+1
                else:
                    r = m
            return arr[l] if l < len(arr) else -1
        
        MAX = 1000000000
        arr2.sort()
        dp = {arr1[0]: 0}
        if arr2[0] < arr1[0]:
            dp[arr2[0]] = 1
        
        n = len(arr1)
        for i in range(1, n):
            #print(dp)
            dp2 = dict()
            for num in dp:
                #no replace
                if num < arr1[i]:
                    dp2[arr1[i]] = min(dp2.get(arr1[i], MAX), dp[num])
                #replace: binary search to find the best option
                val = upperBound(arr2, num)
                if val != -1:
                    dp2[val] = min(dp2.get(val, MAX), dp[num]+1)
            dp = dp2
        
        if not dp: #empty solution set
            return -1
        
        min_ops = n
        for n_ops in dp.values():
            min_ops = min(min_ops, n_ops)
        return min_ops
        
                
                    
                
            
        
        