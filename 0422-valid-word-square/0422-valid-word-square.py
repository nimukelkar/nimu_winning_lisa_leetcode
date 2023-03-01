class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        newword = []
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i < len(words[j]):
                    newword.append(words[j][i])
            res.append(''.join(newword))
            newword = []
        
        return words == res