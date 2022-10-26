class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        n = len(nums)
        prefix = 0
        for i in range(n):
            prefix = (prefix + nums[i])%k
            if prefix not in dic:
                dic[prefix] = i
            else:
                if (i - dic[prefix]) >= 2:
                    return True
        return False