class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global_max=0
        left=0
        n=len(s)
        d={}

        for i in range(n):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1

            while(d[s[i]]>1 and left<=i):
                d[s[left]]-=1
                left+=1
            
            local_len=i-left+1
            global_max=max(global_max,local_len)
        return global_max

