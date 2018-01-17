'''
448. Find All Numbers Disappeared in an Array
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        for x in xrange(l):
            nums[abs(nums[x])-1]*=-1
            if nums[abs(nums[x])-1]>0:
                nums[abs(nums[x])-1]*=-1
        return [x+1 for x in xrange(l) if nums[x]>0]