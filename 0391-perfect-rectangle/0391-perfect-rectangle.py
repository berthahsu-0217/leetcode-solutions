class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        area = 0
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            #print((x2-x1)*(y2-y1))
            area += (x2-x1)*(y2-y1)
            corners ^= {(x1,y1),(x1,y2),(x2,y1),(x2,y2)}
            
        if len(corners) != 4:
            return False
        
        corners = sorted(list(corners), key = lambda x: (x[0]+x[1]))
        
        return area == ((corners[-1][0]-corners[0][0])*(corners[-1][1]-corners[0][1]))