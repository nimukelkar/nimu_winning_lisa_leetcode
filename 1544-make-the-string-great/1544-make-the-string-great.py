class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i].swapcase():
                stack.pop(-1)
            else:
                stack.append(s[i])
        return ''.join(stack)