class SimpleIntHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_function(self, value):
        return value % self.size

    def insert(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        index = self.hash_function(value)
        bucket = self.table[index]
        if value not in bucket:
            bucket.append(value)
            self.count += 1

    def search(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        index = self.hash_function(value)
        return value in self.table[index]

    def delete(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        index = self.hash_function(value)
        bucket = self.table[index]
        if value in bucket:
            bucket.remove(value)
            self.count -= 1
            return True
        return False

    def values_at_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        return self.table[index]

    def load_factor(self):
        return self.count / self.size

    def display(self):
        print("\nHash Table State (index acts as key):")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


if __name__ == "__main__":
    ht = SimpleIntHashTable(size=10)

    print("Inserting values...")
    ht.insert(15)
    ht.insert(25)
    ht.insert(15)
    ht.insert(75)
    ht.insert(45)
    ht.insert(25)
    ht.insert(5)
    ht.insert(32)
    ht.insert(51)
    ht.insert(66)
    ht.insert(88)
    ht.insert(97)
    ht.insert(30)
    ht.insert(36)

    print("\nHash Table after insertions:")
    ht.display()