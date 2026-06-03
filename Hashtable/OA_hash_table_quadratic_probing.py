class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        original_index = self.hash_function(key)
        for i in range(self.size):  
            index = (original_index + i * i) % self.size
            if self.table[index] is None:
                self.table[index] = key
                return
        print("Hash Table is Full! Cannot insert", key)

    def search(self, key):
        original_index = self.hash_function(key)
        for i in range(self.size):
            index = (original_index + i * i) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return True
        return False

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

if __name__ == "__main__":
    ht = QuadraticProbingHashTable(10)

    ht.insert(15)
    ht.insert(25)
    ht.insert(35)
    ht.insert(45)
    ht.insert(55)
    ht.insert(65)
    ht.insert(75)
    ht.insert(85)
    ht.insert(95)
    ht.insert(105)  # This will cause a collision and test the quadratic probing
    ht.insert(115)  # This should indicate that the table is full
    ht.insert(125)  # This should also indicate that the table is full
    ht.display()
    print("Search 25:", ht.search(25))