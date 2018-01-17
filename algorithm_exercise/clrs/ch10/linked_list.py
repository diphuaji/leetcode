class Element:
    def __init__(self,k=None):
        self.next=None     
        self.key=k
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,k):
        e =Element(k)
        e.next=self.head
        self.head=e
        if self.tail is None:
            self.tail=self.head
        
    def search(self,k):
        e=self.head
        while e is not None:            
            if e.key==k:
                return e.key
            e=e.next
        return e
    def delete(self,k):
        prev=None
        e=self.head
        while e is not None:
            if e.key==k:
                if prev is not None:
                    prev.next=e.next
                else:
                    self.head=e.next
                if e.next is None:
                    self.tail=prev
                return
            prev=e
            e=e.next
if __name__=='__main__':
    l=LinkedList()
    print 'insert 5'
    l.insert(5)
    print l.head.key
    print 'insert 8'
    l.insert(8)
    print l.head.key
    print 'insert 120'
    l.insert(120)
    print l.head.key
    print 'insert 21'
    l.insert(21)
    print 'del 21'
    l.delete(21)
    print l.head.key
    print 'del 120'
    l.delete(120)
    print l.head.key

