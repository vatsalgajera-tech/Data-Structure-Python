class SimpleHashTable:
	def __init__(self, size=8):
		self.size = size
		self.table = [[] for _ in range(size)]
		self.count = 0  # Number of stored key-value pairs.

	def hash_function(self, key):
		key_str = str(key)
		hash_value = 0
		for i, ch in enumerate(key_str):
			hash_value += (i + 1) * ord(ch)
		return hash_value % self.size

	def insert(self, key, value):
		index = self.hash_function(key)
		bucket = self.table[index]

		for pair in bucket:
			if pair[0] == key:
				pair[1] = value
				return

		bucket.append([key, value])
		self.count += 1

	def get(self, key):
		index = self.hash_function(key)
		bucket = self.table[index]

		for pair in bucket:
			if pair[0] == key:
				return pair[1]
		return None

	def delete(self, key):
		index = self.hash_function(key)
		bucket = self.table[index]

		for i, pair in enumerate(bucket):
			if pair[0] == key:
				del bucket[i]
				self.count -= 1
				return True
		return False

	def load_factor(self):
		return self.count / self.size

	def display(self):
		print("\nHash Table State:")
		for i, bucket in enumerate(self.table):
			print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
	ht = SimpleHashTable(size=7)

	print("Inserting key-value pairs...")
	ht.insert("name", "Himanshu")
	ht.insert("city", "Nadiad")
	ht.insert("course", "Data Structures")
	ht.insert("age", 19)

	ht.display()
	print(f"\nLoad Factor: {ht.load_factor():.2f}")

	print("\nRetrieving keys:")
	print("name ->", ht.get("name"))
	print("city ->", ht.get("city"))
	print("unknown ->", ht.get("unknown"))

	print("\nUpdating 'city' and deleting 'age'...")
	ht.insert("city", "Ahmedabad")
	ht.delete("age")

	ht.display()
	print(f"\nLoad Factor after update/delete: {ht.load_factor():.2f}")
