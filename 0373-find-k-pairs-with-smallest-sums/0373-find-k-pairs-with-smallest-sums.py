import heapq as hq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return self.solution1(nums1, nums2, k)
    
    def solution1(self, nums1, nums2, k):
        """
        Solution 1
        i
        1 4 5 6 9
        2 2 3 4 7
        j
        
        i = 0 [[1,2],[1,2],[1,3],[1,4],[1,7]]
        i = 1 [[4,2],[4,2],[4,3],[4,4],[4,7]]
        i = 2 [[5,2],[5,2],...]
        i = 3 ...
        i = 4 ...
        
        => find first k smallest elements in m sorted lists of length n
        """
        pairs = []
        m, n = len(nums1), len(nums2)
        
        #O(m)
        min_heap = [(nums1[i]+nums2[0], i, 0) for i in range(m)]
        hq.heapify(min_heap)

        #O(klogm)
        for t in range(min(k, m*n)):
            _, i, j = hq.heappop(min_heap)
            pairs.append([nums1[i], nums2[j]])
            if j+1 < n:
                hq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
                
        return pairs
                
        