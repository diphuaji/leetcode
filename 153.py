'''
153. Find Minimum in Rotated Sorted Array
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        minV=nums[0]
        for i in xrange(len(nums)-1):
            if nums[i]>nums[i+1] and minV>nums[i+1]:
                return nums[i+1]
        return minV
