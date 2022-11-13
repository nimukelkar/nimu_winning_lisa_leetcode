class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        l=list(s.split(" "))
        print(l)
        l1=[]
        for i in l:
            if i!="":
                l1.append(i)
        ptr1=0
        ptr2=len(l1)-1
        
        while(ptr1<ptr2):
            l1[ptr1],l1[ptr2]=l1[ptr2],l1[ptr1]
            ptr1+=1
            ptr2-=1
        return " ".join(l1)