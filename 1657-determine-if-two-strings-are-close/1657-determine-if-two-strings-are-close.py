class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:          
                                                                     

        c1 = Counter(word1)                                         #          c1 = {'a':2, 'b':3, 'c':1}
        c2 = Counter(word2)                                         #          c1 = {'a':2, 'b':3, 'c':1}

        count1 = sorted(c1.values())                                #      count1 = [1, 2, 3]
        count2 = sorted(c2.values())                                #      count2 = [1, 2, 3]

        set1 = set(word1)                                           #        set1 = {'c', 'b', 'a'}
        set2 = set(word2)                                           #        set2 = {'a', 'c', 'b'}

        if count1 == count2 and set1 == set2:                       #      return True
            return True

        return False