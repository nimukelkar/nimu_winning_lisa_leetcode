class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points=0
        local_sum=0
        
        for i in range(k):
            local_sum+=calories[i]
        if local_sum>upper:
            points+=1
        if local_sum<lower:
            points-=1
            
        
        for i in range(k,len(calories)):
            local_sum=local_sum+calories[i]-calories[i-k]
            
            if local_sum>upper:
                points+=1
            elif local_sum<lower:
                points-=1
        return points