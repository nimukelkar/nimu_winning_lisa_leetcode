class Solution:
    def simplifyPath(self, path: str) -> str:
        #case 1. remove trailing slash
        #case 2. if ".." comes at first, remove it
        #case 3. if  ".." comes at middle or end, then we need to go back one level. sometimes output can be empty,             in such case handle it like case 2
        #case 4: if "." or "" comes, then just ignore it
        #case 5: if output is empty make sure to add a /, because the output format is stricly a canonical path

        l=path.split("/")
        print(l)
        stk=[]
        ans=""
    
        for i in l:
            if i==".." and len(stk)>0:
                #print(ans)
                stk.pop()
                continue
            elif i!=".." and i!="" and i!=".":
                #print("i=",i)
                stk.append(i)
        for i in stk:
            ans+='/'+i
        if not ans or ans[0]!="/":
            return "/"+ans
        return ans
     
           
                
        
            