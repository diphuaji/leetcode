class DeQueue:
    def __init__(self,size=10):
        self.head=self.tail=0
        self._array=[0 for i in xrange(size+1)]
    def enqueue(self,e):        
        if (self.tail+1)%(len(self._array))==self.head:
            raise Exception('queue overflowed!')        
        self._array[self.tail]=e
        self.tail=(self.tail+1)%(len(self._array))
    def dequeue(self):
        if self.tail==self.head:
            raise Exception('queue underflowed!')
        self.head=(self.head+1)%(len(self._array))
        return self._array[self.head-1]
    def enqueueR(self,e):        
        if (self.tail+1)%(len(self._array))==self.head:
            raise Exception('queue overflowed!')   
        if self.head-1<0:
            self.head=len(self._array)+self.head-1
        else:
            self.head= self.head-1
        self._array[self.head]=e
    def dequeueR(self):
        if self.tail==self.head:
            raise Exception('queue underflowed!')
        if self.tail-1<0:
            self.tail=len(self._array)+self.tail-1
        else:
            self.tail= self.tail-1
        return self._array[self.tail]
q=DeQueue(5)
q.enqueue(1)
q.enqueueR(3)
q.dequeueR()
q.dequeue()
q.dequeue()
print q._array,q.tail,q.head
