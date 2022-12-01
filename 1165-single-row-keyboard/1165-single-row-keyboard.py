from collections import *
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d=defaultdict(int)
        
        for i in range(len(keyboard)):
            d[keyboard[i]]=i
        #print(d)
        
        count=0
        count+=d[word[0]]
        for i in range(1,len(word)):
            count+=abs(d[word[i]]-d[word[i-1]])
        return count
            