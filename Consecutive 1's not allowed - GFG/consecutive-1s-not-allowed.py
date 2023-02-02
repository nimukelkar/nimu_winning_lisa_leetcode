#User function Template for python3
class Solution:

	def countStrings(self,n):
	    if n==1:
	        return 2
    	# code here
        table0=[0 for i in range(n)]
        table1=[0 for i in range(n)]
        #print("Table1=",table1,"table2=",table2)

        table0[0] = 1
        table1[0] = 1
        for i in range(1,n):
            table0[i]=(table0[i-1]+table1[i-1])%1000000007
            table1[i]=table0[i-1]
        #print("table0=",table0)
        #print("table1=",table1)
        #print("Result=",table0[n-1]+table1[n-1])
        return (table0[n-1]+table1[n-1])%1000000007

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends