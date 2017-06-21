'''
605. Can Place Flowers
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n: return True
        left=0
        for i in xrange(len(flowerbed)-1):
            if flowerbed[i]:
                left=1
                continue
            if left+flowerbed[i+1]:
                left=0
                continue
            n-=1
            if not n:
                return True
            left=1
        left=not(left+flowerbed[-1])
        return not(n-left)