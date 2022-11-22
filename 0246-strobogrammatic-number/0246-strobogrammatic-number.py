class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        flag=1
        ptr1=0
        ptr2=len(num)-1
        if len(num)==1:
            if num=="0"  or num=="8" or num=="1":
                return True
            return False
        while(ptr1<=ptr2):
            if num[ptr1] in d:
                if num[ptr2] in d:
                    if d[num[ptr1]]==num[ptr2]:
                        ptr1+=1
                        ptr2-=1
                        if ptr1>ptr2:
                            break
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return True