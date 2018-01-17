'''
628. Maximum Product of Three Numbers
'''
class Solution(object):
    def maxDistance(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        minus=[]
        positive=[]
        zero=[]
        while len(nums):
            v=nums.pop()
            if v>0:
                positive.append(v)
                continue
            if v<0:
                minus.append(v)
                continue
            zero.append(v)
        temp=0
        if len(positive)>1:
            for i in xrange(min(3,len(positive)-1)):
                for j in xrange(len(positive)-1,i,-1):
                    if positive[j]>positive[j-1]:
                        temp=positive[j-1]
                        positive[j-1]=positive[j]
                        positive[j]=temp
        if len(minus)>1:
            for i in xrange(min(3,len(minus)-1)):
                for j in xrange(len(minus)-1,i,-1):
                    if minus[j]<minus[j-1]:
                        temp=minus[j-1]
                        minus[j-1]=minus[j]
                        minus[j]=temp
        if len(minus)+len(positive)<3:
            return 0
        if len(positive)>2:
            if len(minus)>1:
                return max(positive[0]*positive[1]*positive[2],minus[0]*minus[1]*positive[0])
            return positive[0]*positive[1]*positive[2]
        if len(positive)>0 and len(minus)>1:
            return positive[0]*minus[0]*minus[1]
        if len(zero)==0:
            return minus[0] *minus[1]*minus[2]
        return 0
s=Solution()
