class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def backtrack(arr, val):
            
            if val > high:
                return 0
            
            ways = 0
            
            if low <= val <= high:
                if len(arr) == 2 and arr[0] == arr[1]:
                    ways += 1
                if len(arr) == 4 and arr[0]+arr[1] == arr[2]+arr[3]:
                    ways += 1

            for i in range(10):
                if len(arr) == 0 and i == 0:
                    continue
                arr.append(i)
                ways += backtrack(arr, val*10+i)
                arr.pop()
                
            return ways

        return backtrack([], 0)