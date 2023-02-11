class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        if len(set(fruits)) < 3:
            return len(fruits)
        
        basket = {fruits[0], fruits[1]}
        count = 2
        i = 2               
        n = len(fruits)
        count, maxcount = 0,0
        i = 0
        while(i < n):
            
            if len(basket) <= 2:
                basket.add(fruits[i])
                count+=1
                i+=1
            
            if len(basket) == 3:
                count-=1
                i = i-1
                maxcount = max(count, maxcount)
                count    = 0
                basket.remove(fruits[i])
                basket.remove(fruits[i-1])
                i = i-1
                
                while (fruits[i] not in basket):
                    i -=1
                i+=1
                basket = set()
        
        return max(maxcount, count)