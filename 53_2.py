class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        sum_to_substract = 0
        for i in xrange(len(nums)):
            if i != 0:
                nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i]-sum_to_substract)
            if nums[i] < 0:
                sum_to_substract = min(sum_to_substract, nums[i])
        return maxSum
