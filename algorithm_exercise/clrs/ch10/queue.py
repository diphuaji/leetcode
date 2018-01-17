class MyQueue:
    def __init__(self,size=10):
        self.head=self.tail=0
        self._array=[0 for i in xrange(size+1)]
    def empty(self):
        return self.tail==self.head
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
if __name__=='__main__':
    q=MyQueue(5)
    q.enqueue(1)
    for i in xrange(10):
        q.enqueue(2)
