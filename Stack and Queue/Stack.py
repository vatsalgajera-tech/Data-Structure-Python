class Stack:
    def __init__(self,size):
        self.top = -1
        self.size = size
        self.stack = [None] * size
        
    def isEmpty(self):    
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1    
            
    def push(self,data):
        if self.isFull():
            print("Stack is Full.")
            return
        self.top += 1
        self.stack[self.top] = data
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty.")
            return
        self.top -= 1
        
    def peak(self):
        print(f"Peak Element : {self.stack[self.top]}")
        
    def display(self):
        if self.isEmpty():
            print("Stack is Empty.")
            return
        for i in range(self.top,-1,-1):
            print(f"| {self.stack[i]} |")
        print("______\n")
        
    def search(self,data):
        if self.isEmpty():
            print("Stack is Empty.")
            return
        for i in range(self.top+1):
            if self.stack[i] == data:
                print(f"{data} Found at {i} index!")
                return
        return "Data Not Found."
    
size = int(input("Enter the Length of Stack : "))
s = Stack(size)
for i in range(size):
    s.push(int(input("Enter Element : ")))
s.display()
s.pop()
s.pop()
s.display()
s.search(20)
s.search(50)
s.peak()