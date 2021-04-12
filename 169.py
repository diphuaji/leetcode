'''
169. Majority Element 
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        maj = nums[0]
        for i in xrange(1, len(nums)):
            if count == 0:
                count += 1
                maj = nums[i]
            elif nums[i] == maj:
                count += 1
            else:
                count -= 1
        return maj
