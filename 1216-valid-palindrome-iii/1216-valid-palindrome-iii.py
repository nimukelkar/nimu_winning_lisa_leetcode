class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if s == s[::-1]: return True
        
        @lru_cache(None)
        def validPalindrome(s,l,r,numOfChoices):
            nonlocal k
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    if numOfChoices <k:
                        return validPalindrome(s,l+1,r,numOfChoices+1) or validPalindrome(s,l,r-1,numOfChoices+1)
                    elif numOfChoices ==k:  #cannot afford more mistakes
                        return False
            
            return True
            
        
        return validPalindrome(s,0,len(s)-1,0)