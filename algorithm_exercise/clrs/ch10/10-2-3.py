from linked_list import LinkedList
class MyStack:
    def __init__(self):
        self._list=LinkedList()
    def empty(self):
        return self._list.tail==None
    def dequeue(self):
        e = self._list.tail
        if e is not None:
            self._list.delete(e.key)
            return e.key
        return e
    def enqueue(self,k):
        self._list.insert(k)

if __name__=='__main__':
    s=MyStack()
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
