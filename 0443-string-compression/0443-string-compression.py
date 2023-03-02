from collections import *
class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        ptr1=0
        ptr2=1
        if len(chars)==1:
            return 1
        count=1
        while(ptr2!=len(chars)):
            
            if chars[ptr1]==chars[ptr2]:
                count+=1
                ptr1+=1
                ptr2+=1
            else:
                if count>1:
                    s+=chars[ptr1]+str(count)
                else:
                    s+=chars[ptr1]
                ptr1+=1
                ptr2+=1
                count=1
        if count>1:
            s+=chars[ptr1]+str(count)
        else:
            s+=chars[ptr1]
        print("s=",s)
        for i in range (len(s)):
            chars[i]=s[i]
        return len(s)
                