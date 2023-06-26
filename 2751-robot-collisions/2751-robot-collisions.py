class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        """
        positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
        
        
        [0]
        """
        positions = [(x, i) for i, x in enumerate(positions)]
        positions.sort()
        
        #print(positions)
        
        stack = []
        
        for x, i in positions:
            if directions[i] == "L":
                add = True
                while stack and directions[stack[-1]] == "R":
                    j = stack.pop()
                    if healths[j] == healths[i]:
                        add = False
                        break
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        stack.append(j)
                        add = False
                        break
                    else:
                        healths[i] -= 1
                if add:
                    stack.append(i)
            else:
                stack.append(i)
        
        stack.sort()
        return [healths[i] for i in stack]