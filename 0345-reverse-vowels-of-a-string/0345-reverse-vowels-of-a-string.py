class Solution:
    def reverseVowels(self, s: str) -> str:
        ptr1=0
        ptr2=len(s)-1
        s1=list(s)
        while(True):
            if s1[ptr1].lower() in ('a','e','i','o','u') or s1[ptr1].upper() in ('A','E','I','O','U'):
                if s1[ptr2].lower() in ('a','e','i','o','u')or s1[ptr2].upper() in  ('A','E','I','O','U') :
                    s1[ptr1],s1[ptr2]=s1[ptr2],s1[ptr1]
                    ptr1+=1
                    ptr2-=1
                else:
                    ptr2-=1
            else:
                ptr1+=1
            if ptr1>=ptr2:
                break
        return "".join(s1)
                