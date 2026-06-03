class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def count(self):
        if self.head == None:
            return 0
        counter = 1
        curr = self.head
        while curr.next:
            counter += 1
            curr = curr.next
        return counter
        
    def insert_begin(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head = node  
        
    def insert_position(self,data,pos):
        node = Node(data)
        if pos == 1:
            return self.insert_begin(data)
        elif pos == self.count():
            return self.insert_end(data)
        elif pos < 1 or pos > self.count():
            print("Invalid Position.")
            return
        curr = self.head
        for i in range(pos - 2):
            curr = curr.next
        node.next = curr.next
        curr.next = node
        
    def insert_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    
    def search(self,data):
        if self.head == None:
            print("Linkedlist is Empty.")
            return
        curr = self.head
        while curr:
            if curr.data == data:
                print(f"{data} found!")
                return
            curr = curr.next
        print(f"{data} not found")
    
    def delete_begin(self):
        if self.head == None:
            print("Linked List is Empty.")
            return
        self.head = self.head.next
    
    def delete_end(self):
        if self.head == None:
            print("LL is Empty")
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        
    def delete_position(self,pos):
        if self.head == None:
            print("LL IS EMPTY")
            return
        curr = self.head
        for i in range(pos - 2):
            curr = curr.next
        curr.next = curr.next.next    
        
    def display(self):
        if self.head == None:
            print("Linkedlist is Empty!")
            return
        curr = self.head
        while curr:
            print(curr.data,end=" -> ")
            curr = curr.next
        print("None")
    
sll = SLL()
sll.insert_begin(30)
sll.insert_begin(20)
sll.insert_begin(10)
sll.display()
sll.insert_end(40)
sll.insert_end(50)
# sll.display()
# sll.search(50)
# sll.search(25)
# sll.delete_begin()
# sll.display()
# sll.delete_end()
sll.display()
sll.insert_position(25,3)
sll.display()
sll.delete_position(3)
sll.display()