class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyCircularLinkedList:
    def  __init__(self):
        self.head = None
        self.tail = None
        
    def insertEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
            node.next = node.prev = self.head
            return
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head.prev = node
        self.tail = node        
        
    def insertPosition(self,data,position):
        node = Node(data)
        if position > self.count() or position < 1:
            print("Invalid Position")
            return
        elif position == 1:
            return self.insertBegin(data)
        elif position == self.count():
            return self.insertEnd(data)
        else:
            curr = self.head
            for i in range(position - 2):
                curr = curr.next 
            node.next = curr.next
            curr.next = node       
            
    def deletePosition(self,position):
        if self.head == None:
            return None
        elif position > self.count() or position < 1:
            print("Invalid Position")
            return
        elif position == 1:
            return self.deleteFront()
        elif position == self.count():
            return self.deleteEnd()  
        else:
            curr = self.head
            for i in range(position - 2):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
                
    def insertBegin(self,data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
            node.next = node.prev = self.head
            return
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.tail.next = node
        self.head = node            
        
    def deleteEnd(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
                
    def deleteFront(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.head.prev = self.tail         
            
    def count(self):
        if self.head == None:
            return 0
        else:
            c = 1
            curr = self.head
            while curr.next is not self.head:
                c += 1
                curr = curr.next
        return c
    
    def display(self):
        if self.head == None:
            return None
        curr = self.head
        print(f"Head Node : {self.head.data}\nTail Node : {self.tail.data}\nTotal Nodes : {self.count()}\nLinkedList : ",end="")
        while curr.next is not self.head:
            print(curr.data,end=" -> ")
            curr = curr.next
        print(curr.data,"\n")
        
    def search(self,target):
        if self.head == None:
            return None
        curr = self.head
        while curr.next is not self.head:
            if curr.data == target:
                print(f"{target} Found")
                return
            curr = curr.next
        if curr.data == target:
            print(f"{target} Found")
            return
        print(f"{target} Not Found")
        
dcll = DoublyCircularLinkedList()
dcll.insertEnd(30)
dcll.insertEnd(40)
dcll.display()
dcll.insertBegin(20)
dcll.insertBegin(10)
dcll.display()
dcll.deleteEnd()
dcll.display()
dcll.deleteFront()
dcll.display()
dcll.search(30)
dcll.search(20)
print()
dcll.insertPosition(10,1)
dcll.display()
dcll.insertPosition(25,2)
dcll.display()
dcll.insertPosition(40,4)
dcll.display()
dcll.deletePosition(3)
dcll.display()