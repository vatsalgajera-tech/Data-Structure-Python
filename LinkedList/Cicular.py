class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SinglyCircular:
    def __init__(self):
        self.head = None
        
    def insert_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            node.next = self.head
            return
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next
        node.next = self.head
        curr.next = node
        
    def insert_begin(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            node.next = self.head
            return
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next
        node.next = self.head
        curr.next = node
        self.head = node
        
    def display(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.next is not self.head:
            print(curr.data,end=" -> ")
            curr = curr.next
        print(curr.data)
        
    def count(self):
        if  self.head == None:
            return 0
        curr = self.head
        c = 1
        while curr.next is not self.head:
            c += 1
            curr = curr.next
        return c
    
    def search(self,target):
        if self.head is None:
            return None
        curr = self.head
        while curr.next is not self.head:
            if curr.data == target:
                return "FOUND"
            curr = curr.next
        if curr.data == target:
            return "FOUND"
        return "NOT FOUND"
    
    def delete_end(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.next.next is not self.head:
            curr = curr.next
        curr.next = self.head
        
    def delete_begin(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = self.head.next
    
    def delete_pos(self,pos):
        if self.head is None:
            return None
        elif pos < 1 or pos > self.count():
            print("Invalid Position")
            return
        elif pos == 1:
            return self.delete_begin()
        elif pos == self.count()+1:
            return self.delete_end()
        else:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                curr = self.head
                for i in range(pos-2):
                    curr = curr.next
                curr.next = curr.next.next
            
    def insert_pos(self,data,pos):
        node = Node(data)
        if self.head is None:
            return None
        elif pos < 1 or pos > self.count():
            print("Invalid Position")
            return
        elif pos == 1:
            return self.insert_begin(data)
        elif pos == self.count():
            return self.insert_end(data)
        else:
            if self.head.next == self.head:
                self.head.next = node
                node.next = self.head
                return
            else:
                curr = self.head
                for i in range(pos - 2):
                    curr = curr.next
                node.next = curr.next
                curr.next = node
                
            
scl = SinglyCircular()
scl.insert_end(10)
scl.insert_end(20)
scl.insert_end(30)
scl.display()
scl.insert_begin(0)
scl.insert_begin(-10)
scl.display()
# print("Count Nodes : ",scl.count())
# print(scl.search(30))
# print(scl.search(50))
scl.delete_end()
scl.display()
scl.delete_begin()
scl.display()
scl.delete_pos(2)
scl.display()
scl.insert_pos(-10,1)
scl.insert_pos(30,3)
scl.insert_pos(10,3)
scl.display()
scl.delete_pos(5)
scl.display()