'''
621. Task Scheduler
'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        interval=0
        emptyCount=0
        dic={}
        for t in tasks:
            if t in dic:
                dic[t]+=1
                continue
            dic[t]=1
        maxKey=-1
        maxVal=-1
        for k in dic:
            if maxVal<dic[k]:
                maxKey=k
                maxVal=dic[k]
        emptyCount=(maxVal-1)*n
        del dic[maxKey]
        for k in dic:
            emptyCount-=min(dic[k],maxVal-1)
        if emptyCount>0:
            return emptyCount+len(tasks)
        return len(tasks)
            
s=Solution()
print s.leastInterval(['A','B','A','B','B','B','D','D','G','G'],1)
