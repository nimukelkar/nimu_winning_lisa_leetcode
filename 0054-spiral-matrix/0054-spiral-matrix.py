class Solution:
    def spiralOrder(self,arr: List[List[int]]) -> List[int]:
        m=len(arr)
        n=len(arr[0])
        output=[]
        count=0
        fr,fc,lr,lc=0,0,m-1,n-1
        while(fr<=lr and fc<=lc):
            for j in range(fc,lc+1):
                count+=1
                if count>n*m:
                    break
                output.append(arr[fr][j])
            fr+=1

            for  i in range(fr,lr+1):
                count+=1
                if count>n*m:
                    break
                output.append(arr[i][lc])
            lc-=1

            for j in range(lc,fc-1,-1):
                count+=1
                if count>n*m:
                    break
                output.append(arr[lr][j])
            lr-=1

            for i in range(lr,fr-1,-1):
                count+=1
                if count>n*m:
                    break
                output.append(arr[i][fc])
                
            fc+=1
            
        return output