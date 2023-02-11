class Solution:
    def wiggleSort(self, nums):
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)