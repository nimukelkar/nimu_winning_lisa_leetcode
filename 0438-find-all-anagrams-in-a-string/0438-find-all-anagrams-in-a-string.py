class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        d2={}
        l=[]
        ptr1=0
        ptr2=len(p)-1
        s1=s[ptr1:ptr2+1]
        for i in s1:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        
        for i in p:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        if d1==d2:
            l.append(ptr1)
        
        ptr2+=1
        
        while(ptr2<len(s)):
            k=s[ptr2]
            m=s[ptr1]
            #print(k)
            #print(m)
            if k in d2:
                d2[k]+=1
            else:
                d2[k]=1
            d2[m]-=1
            #print("d2[m]",d2[m])
            if d2[m]==0:
                del d2[m]
            #print("d2=",d2)
            if d2==d1:
                l.append(ptr1+1)
            ptr1+=1
            ptr2+=1
        return l
        