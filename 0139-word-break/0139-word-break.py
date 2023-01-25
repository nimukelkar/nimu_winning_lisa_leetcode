class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table=[False for i in range(len(s)+1)]
        
        table[0]=True
        
        for i in range(len(s)+1):
            for j in range(i):
                if table[j]==True and s[j:i] in wordDict:
                    table[i]=True
                    break
        return table[len(s)]