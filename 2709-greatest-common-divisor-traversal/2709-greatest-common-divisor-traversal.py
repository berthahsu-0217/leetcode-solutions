import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        def find_root(disjoint_set, a):
            if disjoint_set[a] != a:
                disjoint_set[a] = find_root(disjoint_set, disjoint_set[a])
            return disjoint_set[a]
        
        def union(disjoint_set, rank, a, b):
            r1 = find_root(disjoint_set, a)
            r2 = find_root(disjoint_set, b)
            if rank[r1] == rank[r2]:
                disjoint_set[r2] = r1
                rank[r1] += 1
            elif rank[r1] > rank[r2]:
                disjoint_set[r2] = r1
            else:
                disjoint_set[r1] = r2
        
        N = len(nums)
        nums = set(nums)
        disjoint_set = {x:x for x in nums}
        rank = {x:1 for x in nums}
        n = len(nums)
        
        MAX = max(nums)
        size = max(nums)+1
        prime = [True]*size
        prime[0] = prime[1] = False
        
        m = math.ceil(max(MAX/2, math.sqrt(MAX)))+1
        for i in range(2, m):
            if prime[i]:
                first_val = i if i in disjoint_set else None
                for j in range(2*i, size, i):
                    if first_val is None and j in disjoint_set:
                        first_val = j
                        continue
                    if first_val and j in disjoint_set:
                        union(disjoint_set, rank, first_val, j)
                    prime[j] = False
        
        roots = set()
        for x in disjoint_set:
            roots.add(find_root(disjoint_set, x))
        
        if len(roots) == 1:
            if roots.pop() == 1:
                return N == 1
            return True
        return False
        
        