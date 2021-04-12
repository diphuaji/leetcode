'''
268. Missing Number 
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = sum(xrange(len(nums)+1))
        while(len(nums)):
            ans = ans - nums.pop()
        return ans
