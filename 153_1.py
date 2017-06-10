'''
153. Find Minimum in Rotated Sorted Array
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1
        mid=h//2
        while h!=l:
            if nums[mid]>nums[h]:
                l=mid+1
            else:
                h=mid
            mid=(l+h)//2
        return nums[mid]
s=Solution()
print s.findMin([4, 5, 6, 7,-5, 0, 1, 2])

