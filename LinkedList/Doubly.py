class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = None
        
    def insert_begin(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    def insert_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.prev = curr
        
    def insert_pos(self,data,pos):
        node = Node(data)
        if pos == 1:
            return self.insert_begin(data)
        elif pos == self.count():
            return self.insert_end(data)
        elif pos < 1 or pos > self.count():
            print("Invalid Index")
            return
        curr = self.head
        for i in range(pos - 2):
            curr = curr.next
        node.next = curr.next
        curr.next = node     
        node.prev = curr
        node.next.prev = node   
        
    def delete_begin(self):
        if self.head ==None:
            return None
        self.head = self.head.next
        self.head.prev = None
        
    def delete_end(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        
    def delete_pos(self,pos):
        if pos < 1 or pos > self.count():
            print("Invalid Position") 
            return
        elif pos == 1:
            return self.delete_begin()
        elif pos == self.count():
            return self.delete_end()
        curr = self.head
        for i in range(pos - 2):
            curr = curr.next
        curr.next = curr.next.next
        curr.next.prev = curr
        
    def display(self):
        if  self.head == None:
            return None
        curr = self.head
        while curr:
            print(curr.data,end=" -> ")
            curr = curr.next
        print("None")
        
    def count(self):
        if self.head == None:
            return 0
        curr = self.head
        c = 1
        while curr.next:
            curr = curr.next
            c+=1
        return c
    
    def search(self,data):
        if self.head == None:
            return "Data not found"
        curr = self.head
        while curr.next:
            if data == curr.data:
                print(f"{data} found")
                return
            curr = curr.next
        print(f"{data} not found")
        
dll = DLL()
dll.insert_begin(30)
dll.insert_begin(20)
dll.insert_begin(10)
dll.display()
dll.insert_end(40)
dll.insert_end(50)
dll.display()
dll.search(30)
dll.search(60)
dll.delete_begin()
dll.display()
dll.delete_end()
dll.display()
dll.insert_pos(35,2)
dll.insert_pos(5,1)
dll.display()
dll.delete_pos(2)
dll.delete_pos(3)
dll.display()