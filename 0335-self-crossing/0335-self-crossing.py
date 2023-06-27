class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        
        """
        case 1: distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]
        The below cases are actually the same if switching angles
        _ _ _
       |     |
       |     |
       |_ _ _|_ _\
             |   /
             |
             
          /|\     
        _ _|_
       |   | |
       |   | |
       |_ _| |
             |   
             |
             
         _ _ _
    /_ _|_ _  |
    \   |   | |
        |_ _| |
              |   
              |
              
         _ _ _
        |  _   |
        | |  | |
        |_| _| |
          |    |   
         \|/   |
        

        case 2: distance[i-1] == distance[i-3] and distance[i]+distance[i-4] >= distance[i-2]     
        _ _ _
       |     |
       |     |
       |    /|\
       |     |
       |_ _ _|   

        case 3: distance[i-2] > distance[i-4] and distance[i-1] <= distance[i-3] and distance[i-5]+distance[i-1] >= distance[i-3] and distance[i]+distance[i-4] >= distance[i-2]
        _ _ _
       |     |
       | /_ _|_ _    
       | \   |   |
       |         |
       |_ _ _ _ _|   
        """
        
        n = len(distance)
        
        d5 = d4 = d3 = d2 = d1 = d0 = 0
        
        for i in range(n):
            d5, d4, d3, d2, d1 = d4, d3, d2, d1, d0
            d0 = distance[i]
            
            #print(d5, d4, d3, d2, d1, d0)
            
            #case 1: distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]
            if i >= 3 and d0 >= d2 and d1 <= d3:
                #print("case1")
                return True
            #case 2: distance[i-1] == distance[i-3] and distance[i]+distance[i-4] >= distance[i-2]   
            elif i >= 4 and d1 == d3 and d0+d4 >= d2:
                #print("case2")
                return True
            #distance[i-2] == distance[i-4] and distance[i-5]+distance[i-1] >= distance[i-3] and distance[i]+distance[i-4] >= distance[i-2]
            elif i >= 5 and d2 > d4 and d1 <= d3 and d1+d5 >= d3 and d0+d4 >= d2:
                #print("case3")
                return True
            

            
        
        return False
                
            
                
        
            
            