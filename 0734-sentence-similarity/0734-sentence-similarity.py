class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        flag=0
        if len(sentence1)==len(sentence2):
            n=len(sentence1)
            for i in range(n):
                if sentence1[i]==sentence2[i]:
                    continue
                else:
                    flag=1
            if flag==0:
                return True
            
            else:
                flag1=1
                for i in range(n):
                    l1=[sentence1[i],sentence2[i]]
                    l2=[sentence2[i],sentence1[i]]
                   
                    if l1 in similarPairs or l2 in similarPairs or sentence1[i]==sentence2[i] :
                        continue
                    else:
                        print("In else","l1=",l1,"l2=",l2)
                        return False
                
                return True
        else:
            return False
    