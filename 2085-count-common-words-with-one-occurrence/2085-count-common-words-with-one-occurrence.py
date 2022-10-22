class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1={}
        d2={}
        count=0
        
        for i in words1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        
        for i in words2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        
        if len(d1)<len(d2):
            mini=d1
            maxi=d2
        else:
            mini=d2
            maxi=d1
        
        for i in mini:
            if i in maxi:
                if mini[i]==1 and maxi[i]==1:
                    count+=1
        return count