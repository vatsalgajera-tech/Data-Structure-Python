class PriorityQueue:
    def __init__(self, size, priorities):
        self.size = size
        self.priorities = priorities    
        self.queues = [[] for _ in range(priorities)]

    def insert(self, value, priority):
        if priority < 1 or priority > self.priorities:
            print("Invalid priority!")
            return    
        if len(self.queues[priority - 1]) >= self.size:
            print(f"Queue for priority {priority} is full!")
            return        
        self.queues[priority - 1].append(value)

    def delete(self):
        for i in range(self.priorities):  # 1 is highest priority
            if self.queues[i]:
                return self.queues[i].pop(0)        
        print("All queues are empty!")
        return None

    def peek(self):
        for i in range(self.priorities):
            if self.queues[i]:
                return self.queues[i][0]
        return None

    def display(self):
        for i in range(self.priorities):
            print(f"Priority {i+1}: {self.queues[i]}")
            
q = PriorityQueue(10, 3)

q.insert(10, 2)
q.insert(5, 1)
q.insert(20, 3)
q.insert(15, 1)
q.display()

print("Deleted:", q.delete())  # from priority 1
print("Deleted:", q.delete())  # from priority 1
print("Deleted:", q.delete())  # from priority 2
q.display()

print(q.peek())