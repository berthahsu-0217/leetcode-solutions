import queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegrees = [set() for i in range(numCourses)]
        outdegrees = [set() for i in range(numCourses)]
        
        for a, b in prerequisites:
            indegrees[b].add(a)
            outdegrees[a].add(b)
            
        q = queue.Queue()
        for i in range(numCourses):
            if len(indegrees[i]) == 0:
                q.put(i)
        
        courses = 0
        while not q.empty():
            node = q.get()
            courses += 1
            for next_node in outdegrees[node]:
                indegrees[next_node].remove(node)
                if len(indegrees[next_node]) == 0:
                    q.put(next_node)
        
        return courses == numCourses
        
        