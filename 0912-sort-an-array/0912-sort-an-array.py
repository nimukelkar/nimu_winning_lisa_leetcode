
class Solution:
    def merge(self,arr,low,mid,high):
        i=low
        j=mid+1
        aux=[]
    
        while(i<=mid and j<=high):
            if arr[i]<=arr[j]:
                aux.append(arr[i])
                i+=1
            else:
                aux.append(arr[j])
                j+=1
        while(i<=mid):
            aux.append(arr[i])
            i+=1
        while(j<=high):
            aux.append(arr[j])
            j+=1
        count=0
        for i in range(low,high+1):
            arr[i]=aux[count]
            count+=1
            if count==len(aux):
                break
        #print("aux=",aux)
        #print("arr=",arr)   
        
    
    def mergesort(self,arr,low,high):
    
        if low>=high:
            return
        mid=(low+high)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,high)
        self.merge(arr,low,mid,high)

    def sortArray(self, arr: List[int]) -> List[int]:
        low=0
        high=len(arr)-1
        self.mergesort(arr,low,high)
        return arr