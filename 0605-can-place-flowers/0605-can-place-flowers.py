class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count,previous=0,0 
        #Count-no of flowers we can plant
        # Prev-what was on prev
        
        for current in flowerbed:
            if current==1:
                if previous==1:
                    count-=1
                previous=1
            else:
                if previous==1:# can't plant
                    previous=0
                else:
                    count+=1
                    previous=1
        if count>=n:
            return True
        return False