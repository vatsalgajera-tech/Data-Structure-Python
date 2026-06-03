class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 7 - (key % 7)  # second hash (should not be 0)

    def insert(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[index] is not None:
            index = (index + i * step) % self.size
            i += 1

        self.table[index] = key

    def search(self, key):
        index = self.hash1(key)
        step = self.hash2(key)

        i = 0
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + i * step) % self.size
            i += 1
            if index == start:
                return False
        return False

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


if __name__ == "__main__":
    ht = DoubleHashingHashTable(10)

    ht.insert(15)
    ht.insert(25)
    ht.insert(35)
    ht.insert(45)

    ht.display()
    print("Search 35:", ht.search(35))