''' 
26. Remove Duplicates from Sorted Array
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        repIndex=0
        for i in xrange(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if repIndex>0:
                    nums[repIndex]=nums[i]
                    repIndex+=1
                continue
            if repIndex==0:
                repIndex=i
        if repIndex==0:
            return len(nums)
        return repIndex