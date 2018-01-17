'''
217. Contains Duplicate 
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2: return False
        nums=sorted(nums)
        for i in xrange(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False