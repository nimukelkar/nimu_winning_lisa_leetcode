class Solution:
    def convert(self, s: str, n: int) -> str:
        if(n==1):
            return s
        ans=["" for i in range(n)]
        x=0
        bl=True
        for i in range(len(s)):
            if(bl and x==n):
                bl=False
                x-=1
            if(not bl and x==0):
                x+=1
                bl=True
            if(bl):
                ans[x]+=s[i]
                x+=1
            else:
                x-=1
                ans[x]+=s[i]
        s=""
        for i in ans:
            s+=i
        return s