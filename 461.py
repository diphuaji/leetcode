'''
461.Hamming Distance
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum([int(x) for x in bin(x^y) if x=='1'])
