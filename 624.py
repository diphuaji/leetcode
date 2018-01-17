'''
624. Maximum Distance in Arrays
'''
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        tails=[]
        heads=[]
        for i in xrange(4):
            for j in xrange(len(arrays)):
                if len(arrays[j])==0: 
                    continue
                if i <2:
                    if i==1 and heads[0][1]==j:
                        continue
                    if len(heads)==i:
                        heads.append([arrays[j][0],j])
                    if heads[i][0]>arrays[j][0]:
                        heads[i]=[arrays[j][0],j]
                    continue
                if i==3 and tails[0][1]==j:
                    continue
                if len(tails)==i-2:
                    tails.append([arrays[j][-1],j])
                    continue
                if tails[i-2][0]<arrays[j][-1]:
                    tails[i-2]=[arrays[j][-1],j]
        if tails[0][1]==heads[0][1]:
            return max(abs(tails[1][0]-heads[0][0]),abs(tails[0][0]-heads[1][0]))
        return abs(tails[0][0]-heads[0][0])