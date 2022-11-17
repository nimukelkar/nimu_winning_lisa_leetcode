
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        l=[]
        
        
        def dfs(menu,i,slate):
            if i==n:
                l.append(slate.copy())
                return
            
            
            #Don't include element in slate
            
            dfs(menu,i+1,slate)
            
            #Include in menu
            
            slate.append(menu[i])
            dfs(menu,i+1,slate)
            slate.pop()
            
            
        dfs(nums,0,[])
        return l
           
                
            