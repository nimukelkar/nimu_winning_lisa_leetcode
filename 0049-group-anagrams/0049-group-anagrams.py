class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d={}
        
        for i in strs:
            i_sorted=str(sorted(i))
            
            if i_sorted not in d:
                d[i_sorted]=[i,]
            else:
                d[i_sorted].append(i)
        return d.values()