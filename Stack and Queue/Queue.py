class Queue:
    def __init__(self,size):
        self.size = size
        self.front = self.rear = -1
        self.queue = [None] * size
        
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return self.rear == self.size - 1
    
    def enqueue(self,data):
        if self.isFull():
            print("Queue is Full.")
            return
        if self.front == -1:
            self.front += 1
        self.rear += 1
        self.queue[self.rear] = data
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
            return
        self.front += 1
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        for i in range(self.front , self.rear + 1):
            print(f"{self.queue[i]} | " , end="")
        print()
            
    def search(self,data):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        for i in range(self.front,self.rear+1):
            if data == self.queue[i]:
                print(f"{data} found at {i} index.")
                return
        return "Data Not Found."
    
size = int(input("Enter the Length of Queue : "))
q = Queue(size)
for i in range(size):
    q.enqueue(int(input("Enter Element : ")))
q.display()
q.dequeue()
q.dequeue()
q.display()
q.search(20)
q.search(50)