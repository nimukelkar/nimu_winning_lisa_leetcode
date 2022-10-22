from heapq import *
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        heapify(nums)
        for i in range(len(nums)):
            
            a=heappop(nums)
            l.append(a)
        return l