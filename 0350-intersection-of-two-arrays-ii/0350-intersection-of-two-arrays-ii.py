class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        if len(nums1)<len(nums2):
            mini=nums1
            maxi=nums2
        else:
            mini=nums2
            maxi=nums1
        
        
        for i in mini:
            if i in maxi:
                l.append(i)
                maxi.remove(i)
        return l
            