class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        previous_num = nums[0]
        previous_pos = 1
        for i in xrange(len(nums)):
            if i:
                if previous_num != nums[i]:
                    nums[previous_pos] = nums[i]
                    previous_pos += 1
            previous_num = nums[i]
        return previous_pos
