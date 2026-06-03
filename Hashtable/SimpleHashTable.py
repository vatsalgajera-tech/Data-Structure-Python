class SimpleHashTable:
	def __init__(self, size=10):
		self.size = size
		self.table = [[] for _ in range(size)]

	def _hash(self, key):
		return hash(key) % self.size

	def insert(self, key, value):
		index = self._hash(key)
		bucket = self.table[index]
		for item in bucket:
			if item[0] == key:
				item[1] = value
				return

		bucket.append([key, value])

	def get(self, key):
		index = self._hash(key)
		bucket = self.table[index]

		for item in bucket:
			if item[0] == key:
				return item[1]

		return None

	def delete(self, key):
		index = self._hash(key)
		bucket = self.table[index]

		for i, item in enumerate(bucket):
			if item[0] == key:
				del bucket[i]
				return True

		return False

	def display(self):
		print("\nHash Table Contents:")
		for i, bucket in enumerate(self.table):
			print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
	ht = SimpleHashTable(size=7)

	print("Inserting values...")
	ht.insert("name", "Aarav")
	ht.insert("city", "Rajkot")
	ht.insert("course", "Data Structures")
	ht.insert("age", 20)
	ht.display()

	print("\nGet values:")
	print("name ->", ht.get("name"))
	print("city ->", ht.get("city"))
	print("missing_key ->", ht.get("missing_key"))

	print("\nUpdating key 'city'...")
	ht.insert("city", "Ahmedabad")
	print("city ->", ht.get("city"))

	print("\nDeleting key 'age'...")
	deleted = ht.delete("age")
	print("Deleted:", deleted)
	ht.display()
