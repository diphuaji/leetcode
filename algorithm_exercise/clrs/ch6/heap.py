#max-heap
class MaxHeap():
    def __init__(self):
        self._array=[]
        self.heap_size=0
    def _parent(self,i):
        if i <1: return None
        if i >self.heap_size:
            raise Exception('heap overflow')
        return int((i-1)/2)
    def _left(self,i):
        if 2*(i+1)-1 >self.heap_size-1: return None
        return 2*(i+1)-1
    def _right(self,i):
        if 2*(i+1)>self.heap_size-1: return None
        return 2*(i+1)
    def build_heap(self,l):
        self.heap_size=len(l)
        self._array=l
        for i in xrange(int(len(l)-1)/2,-1,-1):
            self.heapify(i)     
    def heapify(self,i):
        if i>self.heap_size-1:
            raise Exception('heap underflow')
        largest=i
        lastLargest=None       
        while lastLargest!=largest:
            lastLargest=largest
            if self._left(lastLargest)!=None and self._array[self._left(lastLargest)]>self._array[largest]:                
                largest=self._left(lastLargest)
            if self._right(lastLargest)!=None and self._array[self._right(lastLargest)]>self._array[largest]:
                largest=self._right(lastLargest)
            temp=self._array[lastLargest]
            self._array[lastLargest]=self._array[largest]
            self._array[largest]=temp            
                
    def insert(self,key):
        self.heap_size+=1
        self._array[self.heap_size-1]=0xffffffff
        self.increase_key(self.heap_size-1)
    def extract(self):
        if self.heap_size<1:
            raise Exception('heap underflow')
        val=self.root()
        self.heap_size-=1
        if self.heap_size!=0:            
            self._array[0]=self._array[self.heap_size]        
            self.heapify(0)
        return val
    def root(self):
        if self.heap_size<1:
            raise Exception('heap underflow')
        return self._array[0]
    def increase_key(self,i,key):
        if i >self.heap_size-1:
            raise Exception('heap overflow')
        if key<=self._array[i]:
            raise Exception('new key smaller the old key')
        pos=i
        while self._parent(i)!=None and self._array[self._parent(pos)]<key:
            self._array[pos]=self._array[self._parent(pos)]
            pos=self._parent(pos)
        self._array[pos]=key
#min-heap
class MinHeap():
    def __init__(self):
        self._array=[]
        self.heap_size=0
    def _parent(self,i):
        if i <1: return None
        if i >self.heap_size:
            raise Exception('heap overflow')
        return int((i-1)/2)
    def _left(self,i):
        if 2*(i+1)-1 >self.heap_size-1: return None
        return 2*(i+1)-1
    def _right(self,i):
        if 2*(i+1)>self.heap_size-1: return None
        return 2*(i+1)
    def build_heap(self,l):
        self.heap_size=len(l)
        self._array=l
        for i in xrange(int(len(l)-1)/2,-1,-1):            
            self.heapify(i)     
    def heapify(self,i):
        if i>self.heap_size-1:
            raise Exception('heap underflow')
        largest=i
        lastLargest=None       
        while lastLargest!=largest:
            lastLargest=largest
            #print "--lastLargest:%s--" % (lastLargest)
            if self._left(lastLargest)!=None and self._array[self._left(lastLargest)]<self._array[largest]:                
                largest=self._left(lastLargest)
             #   print "largest pos change to left:%s" % (largest)
            if self._right(lastLargest)!=None and self._array[self._right(lastLargest)]<self._array[largest]:
                largest=self._right(lastLargest)
              #  print "largest pos change to right:%s" % (largest)
            temp=self._array[lastLargest]
            self._array[lastLargest]=self._array[largest]
            self._array[largest]=temp
            #print self._array      
                
    def insert(self,key):
        self.heap_size+=1
        self._array[self.heap_size-1]=0xffffffff
        self.increase_key(self.heap_size-1)
    def extract(self):
        if self.heap_size<1:
            raise Exception('heap underflow')
        val=self.root()
        self.heap_size-=1
        if self.heap_size!=0:            
            self._array[0]=self._array[self.heap_size]        
            self.heapify(0)
        return val
    def root(self):
        if self.heap_size<1:
            raise Exception('heap underflow')
        return self._array[0]
    def decrease_key(self,i,key):
        if i >self.heap_size-1:
            raise Exception('heap overflow')
        if key<=self._array[i]:
            raise Exception('new key smaller the old key')
        pos=i
        while self._parent(i)!=None and self._array[self._parent(pos)]>key:
            self._array[pos]=self._array[self._parent(pos)]
            pos=self._parent(pos)
        self._array[pos]=key

if __name__=="__main__":
    print "test MaxHeap"
    h=MaxHeap()
    h.build_heap([3,4,9,3,7,2,1,99])
    result=""
    while h.heap_size>0:
        result+=str(h.extract())+","
    print result

    print "test MinHeap"
    h=MinHeap()
    h.build_heap([3,4,9,3,7,2,1,99])
    result=""
    while h.heap_size>0:
        result+=str(h.extract())+","
    print result
