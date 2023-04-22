#Sort the array using insertion sort

class Solution:
    def insertionSort(self,arr,n):
        
        for i in range(1,n):
            
            j=i-1
            
            while(j>=0 and arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                j-=1
            
        
    

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends