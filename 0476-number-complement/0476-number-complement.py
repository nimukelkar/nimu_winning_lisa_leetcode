class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)
        print(b)
        b=b[:1]+b[2:]
        print(b)
        s=""
        for i in range(len(b)):
            if b[i]=='0':
                continue
            else:
                new=b[i:]
                break
        #print(new)
        for i in new:
            if i=='0':
                s+='1'
            if i=='1':
                s+='0'
        ans=0
        for i in range(len(s)):
            ans=ans<<1
            ans+=int(s[i])
        return ans