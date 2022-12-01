class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        n=len(s)
        count1,count2=0,0
        
        for i in range(n//2):
            if s[i]=='A' or s[i]=='E'or s[i]=='I' or s[i]=='O' or s[i]=='U'or s[i]=='a'or s[i]=='e' or s[i]=='i'or s[i]=='o'or s[i]=='u':
                count1+=1
        
        for i in range(n//2,n):
            if s[i]=='A' or s[i]=='E'or s[i]=='I' or s[i]=='O' or s[i]=='U'or s[i]=='a'or s[i]=='e' or s[i]=='i'or s[i]=='o'or s[i]=='u':
                count2+=1
        
        
        if count1==count2:
            return True
        return False
            
                