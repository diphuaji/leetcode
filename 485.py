'''
485. Max Consecutive Ones
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxL=l=0        
        for x in nums:
            if x==0:
                maxL=max(maxL,l)
                l=0
                continue
            l+=1
        return max(maxL,l)