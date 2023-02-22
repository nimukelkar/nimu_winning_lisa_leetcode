class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        
        for i in range(len(tokens)):
          
            #print("stk=",stk)
            if tokens[i]!="+" and tokens[i]!="-" and tokens[i]!="*" and tokens[i]!="/": 
                stk.append(tokens[i])
                continue
            else:
                a=int(stk[-1])
                stk.pop()
                b=int(stk[-1])
                stk.pop()
                operator=tokens[i]
                if operator=="+":
                    stk.append(b+a)
                elif operator=="-":
                    stk.append(b-a)
                elif operator=="*":
                    stk.append(b*a)
                else:
                    stk.append(int(b/a))
        return int(stk[0])
        #return stk[0]