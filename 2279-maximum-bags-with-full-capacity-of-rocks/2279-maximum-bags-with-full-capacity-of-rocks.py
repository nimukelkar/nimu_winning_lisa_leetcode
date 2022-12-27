class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
      
        dict={}
        l=[]
        full=0
        for i in range(len(capacity)):

            diff=capacity[i]-rocks[i]
            if(diff<=0):
                full+=1
            else:
                if diff in dict:
                    dict[diff].append(i)
                else:
                    dict[diff]=[i]
        
        

        for k in sorted(dict):
            
            if(k<=additionalRocks):
                l=len(dict[k])
                if((l*k)<=additionalRocks):
                    
                    additionalRocks=additionalRocks-(k*l)
                    dict[k]=[]
                    full+=l
                else:
                    l=len(dict[k])
                    while(additionalRocks>0):
                        additionalRocks=additionalRocks-k
                        if(additionalRocks>=0):
                            full+=1
                        
                    
            
        return(full)

