class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        ans = 0
        
        row_num = n
        col_num = n
        rows = set()
        cols = set()
        
        
        k = len(queries)
        i = k-1
        
        for i in range(k-1, -1, -1):
            t, idx, val = queries[i]
            if t == 0 and idx not in rows:
                ans += col_num*val
                row_num = max(0, row_num-1)
                rows.add(idx)
            elif t == 1 and idx not in cols:
                ans += row_num*val
                col_num = max(0, col_num-1)
                cols.add(idx)
        
        #print(ans)
        return ans
        
        