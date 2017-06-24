from linked_list import LinkedList
class MyStack:
    def __init__(self):
        self._list=LinkedList()
    def empty(self):
        return self._list.tail==None
    def pop(self):
        e = self._list.head.key
        self._list.delete(e)
        return e
    def push(self,k):
        self._list.insert(k)

if __name__=='__main__':
    s=MyStack()
    s.push(2)
    s.push(3)
    s.push(4)
    print s.pop()
    print s._list
