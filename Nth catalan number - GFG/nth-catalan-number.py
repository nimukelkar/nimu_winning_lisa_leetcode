#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        #return the nth Catalan number.
        #C2=C01+C10
        #C3=C0C2+C1C1+C2C0
        table=[0 for i in range(n+1)]
        table[0]=1
        table[1]=1
        
        for i in range(2,n+1):
            s=0
            for j in range(i): #0,1
                s=s+table[j]*table[i-j-1]
            table[i]=s
        
        return table[-1]
                


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