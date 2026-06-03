class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
        
    def isEmpty(self):
        return self.front == -1    
        
    def isFull(self):
        return (self.rear + 1) % self.size == self.front    
        
    def enqueue(self,data):
        if self.isFull():
            print("Queue is Full.")
            return
        if self.front == -1:
            self.front += 1
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
            
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        return self.queue[self.front]
    
    def size(self):
        if self.isEmpty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.size - (self.front - self.rear - 1)
        
    def enqueue_front(self,data):
        if self.isFull():
            print("Queue is Full.")
            return
        if self.front == -1:
            self.front += 1
            self.rear += 1
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.queue[self.front] = data
        
    def dequeue_rear(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size 
            
    def display(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" -> ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
cq.display() 
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.display()
cq.enqueue(60)
cq.enqueue(70)
cq.enqueue(80)
cq.enqueue(90)
cq.enqueue(100)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue_front(50)
cq.display()
cq.dequeue_rear()
cq.display()
