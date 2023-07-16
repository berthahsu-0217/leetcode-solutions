from collections import deque

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    
        m, n = len(req_skills), len(people)
        skill_id = {skill: i for i, skill in enumerate(req_skills)}
        dp = {0:[]}
        
        for i, skills in enumerate(people):
            skill_set = 0
            for skill in skills:
                skill_set |= 1 << skill_id[skill]
            
            for prev_skills, team in dict(dp).items():
                new_skills = prev_skills | skill_set
                if new_skills == prev_skills:
                    continue
                if new_skills not in dp or len(dp[new_skills]) > len(team)+1:
                    dp[new_skills] = team+[i]
        
        return dp[(1 << m)-1]
                
            
            
            
        
        
            
            
            
            
            
        
        
        