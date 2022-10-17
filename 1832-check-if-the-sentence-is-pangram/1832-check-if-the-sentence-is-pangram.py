class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
          ,'r','s','t','u','v','w','x','y','z']
        flag=0
        for i in l:
            if i not in sentence:
                flag=1
                break
        if flag==1:
            return False
        return True
                