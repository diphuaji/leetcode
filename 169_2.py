class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        previous = None
        for num in sorted(nums):
            if num != previous:
                count = 0
            count = count+1
            if count > len(nums)//2:
                return num
            previous = num
