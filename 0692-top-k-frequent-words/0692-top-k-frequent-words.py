class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        l=[]
        words.sort()
        count=0
        
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        print(d)
        for i in d:
            count+=1
            l.append(i)
            if count==k:
                return l
                      