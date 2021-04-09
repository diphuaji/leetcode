'''
283. Move Zeroes
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z_pos = -1
        count = len(nums)
        for i in xrange(count):
            if nums[i] == 0:
                if z_pos < 0:
                    z_pos = i
            elif z_pos >= 0:
                nums[z_pos] = nums[i]
                nums[i] = 0
                if nums[z_pos+1] == 0:
                    z_pos = z_pos+1
