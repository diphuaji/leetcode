'''
53. Maximum Subarray
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        crtSum = 0
        maxSum = -0xffffffff
        for i in nums:
            crtSum += i
            maxSum = max(crtSum, maxSum)
            if crtSum < 0:
                crtSum = 0
        return maxSum


s = Solution()
print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
