class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
