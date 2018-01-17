class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d={}
        keyNum=0
        keyDel=[]
        lastKeyNum=0
        interval=0
        for t in tasks:            
            if t in d:
                d[t]+=1
                continue
            keyNum+=1
            d[t]=1        
        while keyNum>0:
            lastKeyNum=keyNum
            interval+=max(n+1,keyNum)
            for key in d:                
                d[key]-=1
                if d[key]==0:
                    keyNum-=1
                    keyDel.append(key)
            for key in keyDel:
                del d[key]
            if len(keyDel)>0:
                keyDel=[]
        if n+1>keyNum:
            interval-=n+1-lastKeyNum
        return interval
s=Solution()
print s.leastInterval(['A','A','A','B','B','B'],2)
