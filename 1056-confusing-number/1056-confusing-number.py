class Solution:
    def confusingNumber(self, n: int) -> bool:
        s=str(n)
        flag=True
        c=""
        
        for i in s:
            
            if i=='2' or i=='3' or i=='4' or i=='5' or i=='7':
                flag=False
                break
            else:
                if i=="0":
                    c+='0'
                elif i=="1":
                    c+="1"
                elif i=="6":
                    c+="9"
                elif i=="8":
                    c+="8"
                elif i=="9":
                    c+="6"
        print("c=",c)
        if c[::-1]==s:
            flag=False
            return flag
        return flag
                