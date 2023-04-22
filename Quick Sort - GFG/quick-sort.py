#User function Template for python3
import random
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low>=high:
            return
        p=self.partition(arr,low,high)
        self.quickSort(arr,low,p-1)
        self.quickSort(arr,p+1,high)
    
    def partition(self,arr,low,high):
        # code here
        r=random.randint(low,high)
        arr[low],arr[r]=arr[r],arr[low]
        
        pindex=low
        pivot=arr[low]
        curr=pindex+1
        ptr2=high
        
        while(True):
            if arr[curr]<=arr[pindex]:
                curr+=1
                if curr>ptr2:
                    break
            
            if arr[curr]>=arr[pindex]:
                arr[curr],arr[ptr2]=arr[ptr2],arr[curr]
                ptr2-=1
                if curr>ptr2:
                    break
            
           
        arr[pindex],arr[ptr2]=arr[ptr2],arr[pindex]
        return ptr2
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends