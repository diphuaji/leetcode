class Element:
    def __init__(self,key=None):
        self.prev=self.next=None
        self.key=key
class DoubleLinkedList:
    def __init__(self):
        self.nil=Element()
        self.nil.prev=self.nil.next=self.nil
    def insert(self,k):
        e=Element(k)
        e.next=self.nil.next
        e.prev=self.nil
        self.nil.next.prev=e
        self.nil.next=e        
    def search(self,k):
        e=self.nil
        while e.next != self.nil:
            e=e.next
            if e.key==k:
                return k            
        return self.nil.key
    def delete(self,k):
        e=self.nil
        while e.next !=self.nil and e.key!=k:
            e=e.next  
        if e!=self.nil:
            e.prev.next=e.next
            e.next.prev=e.prev
l=DoubleLinkedList()
l.insert(4)
l.insert(5)
l.insert(11)
print l.search(5)
print l.nil.prev.key
print l.nil.next.key
print l.search(111)
print l.search(11)
