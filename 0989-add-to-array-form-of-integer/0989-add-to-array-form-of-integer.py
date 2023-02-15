class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        l=[]
        for i in num:
            s+=str(i)
        ans=int(s)+k
        
        for i in str(ans):
            l.append(int(i))
        return l
        