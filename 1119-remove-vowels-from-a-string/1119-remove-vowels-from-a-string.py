class Solution:
    def removeVowels(self, s: str) -> str:
        s1=""
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                continue
            else:
                s1+=i
        return s1
            