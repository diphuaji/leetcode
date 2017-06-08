'''
621. Task Scheduler
'''
from Queue import PriorityQueue as PQueue
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        interval=0
        dic={}
        for t in tasks:
            if t in dic:
                dic[t]+=1
                continue
            dic[t]=1
        q=PQueue()
        for key in dic:
            q.put(-dic[key])
        cooldown={}
        while len(cooldown)>0 or q.qsize()>0:
            interval+=1
            if (interval-n-1) in cooldown:
                q.put(cooldown[interval-n-1])
                del cooldown[interval-n-1]
            if q.qsize() >0:
                leftCount=q.get()+1
                if leftCount<0:
                    cooldown[interval]=leftCount
        return interval
s=Solution()
print s.leastInterval(['A','B','A','B','B','B','D','D','G','G'],1)
