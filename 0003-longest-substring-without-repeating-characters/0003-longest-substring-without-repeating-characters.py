class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        left=0
        d={}
        maxi=0
        for i in range(n):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
            
            while(d[s[i]]>1 and left<i):
                d[s[left]]-=1
                left+=1
            local_len=i-left+1
            maxi=max(local_len,maxi)
        return maxi
            
            
            