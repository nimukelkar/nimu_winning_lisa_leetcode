class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        l=[]
        
        def dfs(menu,i,slate):
            if i==n:
                l.append(slate.copy())
                return
            
            
            #Take menu[i] and append to slate
            slate.append(menu[i])
            dfs(menu,i+1,slate)
            slate.pop()
            
            while(i<n-1 and menu[i]==menu[i+1]):
                i+=1
            #Take menu[i] and discard it
            dfs(menu,i+1,slate)
                    
        dfs(nums,0,[])
        return l
                