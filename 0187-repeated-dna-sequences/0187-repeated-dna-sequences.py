class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash=5
        hashv=0
        d1={}
        l=[]
        k=9
        d={
            'A':1,
            'C':2,
            'G':3,
            'T':4
        }
        s1=""
        for i in s:
            s1+=str(d[i])
       
        if(len(s)<10):
            return []
        for i in range(10):
            hashv+=int(s1[i])*(5**k)
            k-=1
        #print(hashv)
        #print(len(s))
        newhash=hashv
        d1[newhash]=1
        for i in range(len(s)-10):
            newhash=(newhash-int(s1[i])*5**9)*5+int(s1[i+10])
            #print(newhash)
            if newhash in d1:
                d1[newhash]+=1
                if s[i+1:i+11] not in l:
                    l.append(s[i+1:i+11])
            else:
                d1[newhash]=1
        #print("d1=",d1)
        return l
            