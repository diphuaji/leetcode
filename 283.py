'''
283. Move Zeroes
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zIndex=-1
        for i in xrange(len(nums)):
            if zIndex<0 and nums[i]==0:
                zIndex=i
                continue
            if nums[i]!=0 and zIndex>=0:
                nums[zIndex]=nums[i]
                zIndex+=1
                nums[i]=0
