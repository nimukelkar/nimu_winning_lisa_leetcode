class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stk.append(s[i])
            
            if s[i]==")":
                if not stk:
                    return False
                if stk[-1]=="(":
                    stk.pop()
                else:
                    return False
            if s[i]=="}": 
                 if not stk:
                    return False
                 if stk[-1]=="{":
                    stk.pop()
                 else:
                    return False
            if s[i]=="]":
                if not stk:
                    return False
                if stk[-1]=="[":
                    stk.pop()
                else:
                    return False
        if not stk:
            return True
        return False