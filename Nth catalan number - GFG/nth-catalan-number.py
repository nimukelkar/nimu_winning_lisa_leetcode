#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        #return the nth Catalan number.
        table=[0 for i in range(n+1)]
        for j in range(n+1):
            if j==0:
                table[0]=1
                continue
            
            
            elif j==1:
                table[1]=1
                continue
                
            else:
                ans=0
                for i in range(j):
                    ans+=table[i]*table[j-i-1]
            table[j]=ans
        #print(table)
        return table[n]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends