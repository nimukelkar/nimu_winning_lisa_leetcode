class Solution:
    def isValid(self, s: str) -> bool:
        
        stk=[]
        if len(s)==1:
            return False
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stk.append(s[i])
                continue
            if s[i]==")":
                if stk:
                    if stk[-1]=="(":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            
            if s[i]=="}":
                if stk:
                    if stk[-1]=="{":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            
            if s[i]=="]":
                if stk:
                    if stk[-1]=="[":
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            
        if stk==[]:
            return True
        return False