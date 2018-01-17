class DHeap:
    def __init__(self,d=3):
        self.heap_size=0
        self._array=[]
        self._d=d
    def _parent(self,i):
        return math.ceil((i-1)/self._d)
    def _hasNext(self,i):
        return i!=self.heap_size and (i-1)%self._d!=0
    def _heapify(self,i):
        lastLargest=None
        largest=i
        val=A[i]
    def build_heap():
        pass
