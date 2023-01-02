class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag=False
        if word.isupper() or word.islower():
            flag=True
            return flag
        for i in range(len(word)):
            if i==0 and word[i].isupper():
                flag=True
            if i>0 and word[i].isupper():
                flag=False
                break
        return flag
                    