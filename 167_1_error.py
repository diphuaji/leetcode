'''
167. Two Sum II - Input array is sorted
maximum recursive depth
'''
class Solution(object):
    def __init__(self):
        self.index1=0
        self.index2=0
        self.countNum=0
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if self.countNum ==0:
            self.countNum+=1
            self.index1=0
            self.index2=len(numbers)-1
        if numbers[self.index1]+numbers[self.index2]==target:
            return self.index1+1,self.index2+1
        elif numbers[self.index1]+numbers[self.index2]<target:
            self.index1+=1
        else: 
            self.index2-=1
        return self.twoSum(numbers,target)
s=Solution()
print s.twoSum([2,4,6],8)