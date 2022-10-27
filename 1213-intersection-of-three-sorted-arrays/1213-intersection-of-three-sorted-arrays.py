class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        l=[]
        l2=[]
        
        for i in arr1:
            if i in arr2:
                l.append(i)
        
        for i in l:
            if i in arr3:
                l2.append(i)
        return l2
        