class Solution:
    def simplifyPath(self, path: str) -> str:
        #case 1. remove trailing slash
        #case 2. if ".." comes at first, remove it
        #case 3. if  ".." comes at middle or end, then we need to go back one level. sometimes output can be empty,             in such case handle it like case 2
        #case 4: if "." or "" comes, then just ignore it
        #case 5: if output is empty make sure to add a /, because the output format is stricly a canonical path

        l=path.split("/")
        print(l)
        ans=""
        for i in l:
            if i==".." and len(ans)>0:
                #print(ans)
                ans=ans[:ans.rindex("/")]
            elif i!=".." and i!="" and i!=".":
                ans+="/"+i
        if not ans:
            return "/"
        return ans
     
           
                
        
            