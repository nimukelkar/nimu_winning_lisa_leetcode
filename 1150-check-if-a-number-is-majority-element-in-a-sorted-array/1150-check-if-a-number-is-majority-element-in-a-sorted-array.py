class Solution:
    def isMajorityElement(self, a: List[int], target: int) -> bool:
        #first occ, last occ
        l=[]
        if len(a)==1 and a[0]!=target:
            return False
        low=0
        high=len(a)-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if(a[mid]<target):
                low=mid+1
            else:
                high=mid-1
        
        if(low<len(a) and a[low]==target):
            l.append(low)
        else:
            l.append(-1)
        
        
        low=0
        high=len(a)-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if(a[mid]>target):
                high=mid-1
            else:
                low=mid+1
        
        if(high>=0 and a[high]==target):
            l.append(high)
        else:
            l.append(-1)
        print(l)
        ans=l[1]-l[0]+1
        
        if ans>len(a)//2:
            return True
        return False
        
        