class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        if len(needle)==1:
            for i in range(len(haystack)):
                if haystack[i]==needle[0]:
                    return i
            return -1
        pattern=""
        text=""
        d={
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
            'i':9,
            'j':10,
            'k':11,
            'l':12,
            'm':13,
            'n':14,
            'o':15,
            'p':16,
            'q':17,
            'r':18,
            's':19,
            't':20,
            'u':21,
            'v':22,
            'w':23,
            'x':24,
            'y':25,
            'z':26,
            
        }
       
        lenp = len(needle)
        k1=lenp-1
        k2=lenp-1
        q =29
        
        index=-1
        
        flag = 0
        hashp, hashv = 0, 0
       
        for i in range(lenp):
            hashp += int(d[needle[i]]) * (q ** k1)
            k1 -= 1
        print("hashp=", hashp)
        for i in range(lenp):
            hashv += int(d[haystack[i]]) * (q ** k2)
            k2 -= 1
        print("hashv=", hashv)
        if hashp == hashv:
            return 0
        newhash = hashv
        for i in range(len(haystack) - lenp):
            newhash = (newhash - int(d[haystack[i]]) * q ** (lenp - 1)) * q + int(d[haystack[i + lenp]])
            if newhash == hashp:
                    print(haystack[i+1:i+lenp+1])
                    return i+1
        return -1