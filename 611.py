'''
611. Valid Triangle Number
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        nums=sorted(nums)
        for k in xrange(len(nums)-1,1,-1):
            j=k-1
            i=0
            while i <j:
                if nums[j]+nums[i]>nums[k]:
                    c+=j-i
                    j-=1
                    continue
                i+=1
        return c
s=Solution()
print s.triangleNumber([64,46,64,44,89,25,21,100,10,58,56,91,35,76,45,76,12,39,75,69,53,60,37,41,21,58,18,75,54,72,3,33,66,91,10,35,45,22,89,27,17,41,37,33,63,61,26,10,94,34,51,81,6,94,68,91,78,18,6,77,7,94,59,32,2,37,98,33,43,96,24,58,3,56,78,83,33,2,28,34,32,62,82,63,4,75,98,8,78,15,68,42,8,75,2,46,83,98,41,29])
                    
        
