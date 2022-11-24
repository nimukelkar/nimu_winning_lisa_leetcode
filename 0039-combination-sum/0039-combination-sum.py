class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        n=len(candidates)
        def dfs(menu,i,slate):
           
            if sum(slate)==target:
                    l.append(slate.copy())
                    return
            if sum(slate)>target:
                return
            
            if i==n:
                return
            
            slate.append(menu[i])
            dfs(menu,i,slate)
            slate.pop()
            
            
            dfs(menu,i+1,slate)
            
        dfs(candidates,0,[])
        return l
                