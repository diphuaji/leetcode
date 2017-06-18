'''
216. Combination Sum III 
'''
class Solution(object):   
    def solve(self,depth,sum,ans,start,solutions,k,n):
        for i in xrange(start,10):
            if depth<k:
                if (sum+i)>=n:                    
                    return      
                self.solve(depth+1,sum+i,ans+[i],i+1,solutions,k,n)
            if sum+i==n:                
                solutions.append(ans+[i])                            
        if(depth==k):
            ans=[]
            
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k >9 or k<1: return []
        maxV=minV=0
        for i in xrange(k+1):
            maxV+=9-(i-1)
            minV+=i
        if maxV<n or minV>n: 
            return []
        solutions=[]
        ans=[]
        self.solve(1,0,ans,1,solutions,k,n)        
        return solutions
s=Solution()
print s.combinationSum3(6,200)
        