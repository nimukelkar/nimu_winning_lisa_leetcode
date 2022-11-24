class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        arr=sorted(arr)
        n=len(arr)
        l=[]
        def dfs(menu,i,slate):
            #Backtracking
            if sum(slate)>target:
                    return
            if sum(slate)==target:
                    l.append(slate.copy())
                    return
            # Base case
            if i==n:
                return
                
            # Include and exclude  
            slate.append(menu[i])
            dfs(menu,i+1,slate)
            slate.pop()
            while(i<n-1 and menu[i]==menu[i+1]):
                i+=1
        
            dfs(menu,i+1,slate)
            
    
        dfs(arr,0,[])
        return l
            
