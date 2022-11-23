class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        l=[]
        
        def dfs(menu,i,slate):
            if i==n:
                if slate not in l:
                    l.append(slate.copy())
                return
            
            
            dfs(menu,i+1,slate)
            
            slate.append(menu[i])
            dfs(menu,i+1,slate)
            slate.pop()
        dfs(nums,0,[])
        return l
                